import gradio as gr
from behavior_video import generate_behavior_text
from behavior_insight import analyze_pet_behavior
from tts_utils import generate_tts_audio
from subtitle_video import add_subtitle_to_video
from video_merge import merge_video_and_audio
from behavior_detector import suggest_behaviors
import whisper


def build_confirmation_text(pet_name, behavior, language="Español"):
    es_map = {
        "Sleeping": "durmiendo",
        "Rolling": "rodando por el suelo",
        "Yawning": "bostezando",
        "Stretching": "estirándose",
        "Sitting still": "sentado y tranquilo",
        "Running toward owner": "corriendo hacia ti",
        "Spinning": "dando vueltas",
        "Head tilt": "inclinando la cabeza",
        "Tongue out (hot)": "sacando la lengua porque tiene calor",
        "Tongue out (cute)": "sacando la lengua de forma tierna",
        "Airplane ears": "con las orejas hacia atrás",
        "Tail tucked": "con la cola entre las patas",
        "Smiling / Grinning": "sonriendo",
        "Showing teeth": "mostrando los dientes",
        "Thinking pose": "pensativo",
        "Poop spin / crouch": "preparándose para hacer caca",
        "Toy": "jugando con un juguete",
        "Other / Mystery": "haciendo algo misterioso"
    }
    action_es = es_map.get(behavior, behavior)
    pet_name = pet_name.strip() if pet_name else "tu mascota"
    return f"Creo que {pet_name} está {action_es}. ¿Correcto?"


def parse_confirmation_answer(text):
    text = (text or "").strip().lower()

    yes_words = ["sí", "si", "correcto", "claro", "exacto", "yes", "yeah"]
    no_words = ["no", "incorrecto", "para nada", "wrong", "nope"]

    if any(word in text for word in yes_words):
        return "yes"
    if any(word in text for word in no_words):
        return "no"
    return "unknown"

whisper_model = None

def transcribe_confirmation_audio(audio_path):
    global whisper_model

    if not audio_path:
        return ""

    if whisper_model is None:
        whisper_model = whisper.load_model("base")

    result = whisper_model.transcribe(audio_path, language="es")
    text = result.get("text", "").strip()
    return text

def auto_suggest_behavior(video):
    ranked = suggest_behaviors(video, top_k=3)

    if not ranked:
        return "## PawPaw no pudo detectar ningún comportamiento.", gr.update(value="Other / Mystery")

    top1 = ranked[0][0]

    result = "## PawPaw cree que tu mascota está...\n\n"
    for i, (behavior, score) in enumerate(ranked):
        if i == 0:
            result += f"• **{behavior}** _(más probable)_\n"
        elif i == 1:
            result += f"• {behavior} _(posible)_\n"
        else:
            result += f"• {behavior}\n"

    return result, gr.update(value=top1)


def process_behavior_video(video, behavior, language, style):
    result_text, hook_line, subtitle_line, tts_line = generate_behavior_text(behavior, language, style)
    subtitled_video_path = add_subtitle_to_video(video, hook_line, subtitle_line)
    audio_path = generate_tts_audio(tts_line, language)
    merged_video_path = merge_video_and_audio(subtitled_video_path, audio_path)
    return result_text, merged_video_path, merged_video_path

def generate_confirmation_audio(question_text):
    if not question_text:
        return None
    return generate_tts_audio(question_text, "Español")

def get_behavior_candidates(video, pet_name):
    ranked = suggest_behaviors(video, top_k=3)
    candidates = [b for b, _ in ranked]

    if not candidates:
        return [], "", "", None, 0, "## No se han obtenido comportamientos candidatos."

    current_index = 0
    current_behavior = candidates[current_index]
    question = build_confirmation_text(pet_name, current_behavior)
    question_audio = generate_confirmation_audio(question)

    suggestion_md = "## PawPaw ya ha hecho una primera predicción\n\n"
    suggestion_md += f"### Creo que {pet_name} está: **{current_behavior}**\n\n"
    suggestion_md += "### Otras opciones posibles:\n"

    for i, behavior in enumerate(candidates):
        if i == 0:
            suggestion_md += f"• **{behavior}** _(predicción actual)_\n"
        else:
            suggestion_md += f"• {behavior}\n"

    return candidates, current_behavior, question, question_audio, current_index, suggestion_md


def handle_confirmation_reply(reply_text, candidates, current_index, pet_name):
    decision = parse_confirmation_answer(reply_text)

    if not candidates:
        return (
            gr.update(),
            "",
            None,
            current_index,
            "No hay comportamientos candidatos.",
            ""
        )

    if current_index >= len(candidates):
        return (
            gr.update(),
            "",
            None,
            current_index,
            "Ya no quedan más candidatos.",
            ""
        )

    if decision == "yes":
        confirmed_behavior = candidates[current_index]
        status_text = f"Comportamiento confirmado: **{confirmed_behavior}**. Ahora puedes pulsar **Dale voz a mi mascota** para generar el vídeo."
        return (
            gr.update(value=confirmed_behavior),
            "",
            None,
            current_index,
            status_text,
            confirmed_behavior
        )

    elif decision == "no":
        current_index += 1
        if current_index < len(candidates):
            next_behavior = candidates[current_index]
            question = build_confirmation_text(pet_name, next_behavior)
            question_audio = generate_confirmation_audio(question)
            status_text = f"La predicción anterior no era correcta. Probamos con: **{next_behavior}**"
            return (
                gr.update(),
                question,
                question_audio,
                current_index,
                status_text,
                ""
            )
        else:
            return (
                gr.update(),
                "",
                None,
                current_index,
                "No hay más opciones. Puedes elegir el comportamiento manualmente en el menú desplegable.",
                ""
            )

    else:
        current_behavior = candidates[current_index]
        question = build_confirmation_text(pet_name, current_behavior)
        question_audio = generate_confirmation_audio(question)
        return (
            gr.update(),
            question,
            question_audio,
            current_index,
            'No lo he entendido. Responde con "claro", "correcto", "yes" o "no".',
            ""
        )


with gr.Blocks() as demo:
    gr.Markdown("# 🐾 PawPaw · PawTalk")
    gr.Markdown("### Sistema de reconocimiento de comportamiento y narración automática para mascotas")

    candidates_state = gr.State([])
    current_index_state = gr.State(0)

    with gr.Tab("Dale voz a mi mascota"):
        gr.Markdown("Sube un vídeo de tu mascota y deja que PawPaw interprete su comportamiento y le dé voz.")

        pet_name_input = gr.Textbox(
            label="Nombre de la mascota",
            placeholder="Por ejemplo: Coco",
            value="Coco"
        )

        video_input = gr.Video(label="Vídeo de la mascota")

        behavior_input = gr.Dropdown(
            choices=[
                "Stretching",
                "Yawning",
                "Rolling",
                "Airplane ears",
                "Spinning",
                "Running toward owner",
                "Tail tucked",
                "Sitting still",
                "Head tilt",
                "Tongue out (cute)",
                "Tongue out (hot)",
                "Smiling / Grinning",
                "Showing teeth",
                "Poop spin / crouch",
                "Thinking pose",
                "Sleeping",
                "Toy",
                "Other / Mystery"
            ],
            value="Stretching",
            label="Comportamiento"
        )

        language_input = gr.Dropdown(
            choices=["中文", "Español", "English"],
            value="Español",
            label="Idioma del vídeo"
        )

        style_input = gr.Dropdown(
            choices=["Cute", "Attitude"],
            value="Cute",
            label="Personalidad de la mascota"
        )

        gr.Markdown("### Paso 1: deja que PawPaw adivine el comportamiento")
        suggest_btn = gr.Button("Adivinar comportamiento")
        suggest_output = gr.Markdown()

        confirmation_question = gr.Textbox(
           label="PawPaw pregunta",
           interactive=False
        )

        question_audio_output = gr.Audio(
           label="PawPaw te habla",
           autoplay=True
        )

        reply_audio = gr.Audio(
           sources=["microphone"],
           type="filepath",
           label="Tu respuesta por voz"
        )

        transcribe_btn = gr.Button("Transcribir respuesta")

        reply_input = gr.Textbox(
           label="Texto reconocido",
           placeholder='Aquí aparecerá el resultado del audio'
        )

        confirm_btn = gr.Button("Confirmar respuesta")
        confirm_status = gr.Markdown()
        confirmed_behavior_text = gr.Textbox(
            label="Comportamiento confirmado",
            interactive=False
        )

        gr.Markdown("### Paso 2: generar el vídeo final")
        generate_btn = gr.Button("Dale voz a mi mascota")
        behavior_output = gr.Markdown()
        video_output = gr.Video(label="Vídeo final con voz")
        file_output = gr.File(label="Descargar vídeo final")

        suggest_btn.click(
            fn=get_behavior_candidates,
            inputs=[video_input, pet_name_input],
            outputs=[
               candidates_state,
               behavior_input,
               confirmation_question,
               question_audio_output,
               current_index_state,
               suggest_output
           ]
       )

        video_input.upload(
            fn=get_behavior_candidates,
            inputs=[video_input, pet_name_input],
            outputs=[
                candidates_state,
                behavior_input,
                confirmation_question,
                question_audio_output,
                current_index_state,
                suggest_output
            ]
        )

        transcribe_btn.click(
            fn=transcribe_confirmation_audio,
            inputs=reply_audio,
            outputs=reply_input
       )

        confirm_btn.click(
            fn=handle_confirmation_reply,
            inputs=[reply_input, candidates_state, current_index_state, pet_name_input],
            outputs=[
                behavior_input,
                confirmation_question,
                question_audio_output,
                current_index_state,
                confirm_status,
                confirmed_behavior_text
            ]
        )

        generate_btn.click(
            fn=process_behavior_video,
            inputs=[video_input, behavior_input, language_input, style_input],
            outputs=[behavior_output, video_output, file_output]
        )


with gr.Blocks() as demo:
    gr.Markdown("# 🐾 PawPaw")
    gr.Markdown("### PawTalk · PawCare · PawTrack · PawMemo")

    candidates_state = gr.State([])
    current_index_state = gr.State(0)

    # =========================
    # PAWTALK
    # =========================
    with gr.Tab("PawTalk"):
        gr.Markdown("## Sistema de reconocimiento de comportamiento y narración automática para mascotas")
        gr.Markdown("Sube un vídeo de tu mascota y deja que PawPaw interprete su comportamiento y le dé voz.")

        pet_name_input = gr.Textbox(
            label="Nombre de la mascota",
            placeholder="Por ejemplo: Coco",
            value="Coco"
        )

        video_input = gr.Video(label="Vídeo de la mascota")

        behavior_input = gr.Dropdown(
            choices=[
                "Stretching",
                "Yawning",
                "Rolling",
                "Airplane ears",
                "Spinning",
                "Running toward owner",
                "Tail tucked",
                "Sitting still",
                "Head tilt",
                "Tongue out (cute)",
                "Tongue out (hot)",
                "Smiling / Grinning",
                "Showing teeth",
                "Poop spin / crouch",
                "Thinking pose",
                "Sleeping",
                "Other / Mystery"
            ],
            value="Stretching",
            label="Comportamiento"
        )

        language_input = gr.Dropdown(
            choices=["中文", "Español", "English"],
            value="Español",
            label="Idioma del vídeo"
        )

        style_input = gr.Dropdown(
            choices=["Cute", "Attitude"],
            value="Cute",
            label="Personalidad de la mascota"
        )

        gr.Markdown("### Paso 1: deja que PawPaw adivine el comportamiento")
        suggest_btn = gr.Button("Adivinar comportamiento")
        suggest_output = gr.Markdown()

        confirmation_question = gr.Textbox(
            label="PawPaw pregunta",
            interactive=False
        )

        question_audio_output = gr.Audio(
            label="PawPaw te habla",
            autoplay=True
        )

        reply_audio = gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Tu respuesta por voz"
        )

        transcribe_btn = gr.Button("Transcribir respuesta")

        reply_input = gr.Textbox(
            label="Texto reconocido",
            placeholder="Aquí aparecerá el resultado del audio"
        )

        confirm_btn = gr.Button("Confirmar respuesta")
        confirm_status = gr.Markdown()

        confirmed_behavior_text = gr.Textbox(
            label="Comportamiento confirmado",
            interactive=False
        )

        gr.Markdown("### Paso 2: generar el vídeo final")
        generate_btn = gr.Button("Dale voz a mi mascota")
        behavior_output = gr.Markdown()
        video_output = gr.Video(label="Vídeo final con voz")
        file_output = gr.File(label="Descargar vídeo final")

        suggest_btn.click(
            fn=get_behavior_candidates,
            inputs=[video_input, pet_name_input],
            outputs=[
                candidates_state,
                behavior_input,
                confirmation_question,
                question_audio_output,
                current_index_state,
                suggest_output
            ]
        )

        video_input.upload(
            fn=get_behavior_candidates,
            inputs=[video_input, pet_name_input],
            outputs=[
                candidates_state,
                behavior_input,
                confirmation_question,
                question_audio_output,
                current_index_state,
                suggest_output
            ]
        )

        transcribe_btn.click(
            fn=transcribe_confirmation_audio,
            inputs=reply_audio,
            outputs=reply_input
        )

        confirm_btn.click(
            fn=handle_confirmation_reply,
            inputs=[reply_input, candidates_state, current_index_state, pet_name_input],
            outputs=[
                behavior_input,
                confirmation_question,
                question_audio_output,
                current_index_state,
                confirm_status,
                confirmed_behavior_text
            ]
        )

        generate_btn.click(
            fn=process_behavior_video,
            inputs=[video_input, behavior_input, language_input, style_input],
            outputs=[behavior_output, video_output, file_output]
        )

    # =========================
    # PAWCARE
    # =========================
    with gr.Tab("PawCare"):
        gr.Markdown("## Información básica de la mascota")
        
        care_name = gr.Textbox(label="Nombre", placeholder="Por ejemplo: Coco")
        care_type = gr.Dropdown(
            choices=["Dog", "Cat", "Other"],
            value="Dog",
            label="Tipo de mascota"
        )
        care_age = gr.Textbox(label="Edad", placeholder="Por ejemplo: 2 años")
        care_weight = gr.Textbox(label="Peso", placeholder="Por ejemplo: 4.5 kg")
        care_breed = gr.Textbox(label="Raza", placeholder="Por ejemplo: Mestizo")
        care_notes = gr.Textbox(label="Notas generales", lines=4, placeholder="Alergias, hábitos, observaciones...")

        care_btn = gr.Button("Mostrar perfil")
        care_output = gr.Markdown()

        def build_pet_profile(name, pet_type, age, weight, breed, notes):
            return f"""
## Perfil de la mascota
- **Nombre:** {name}
- **Tipo:** {pet_type}
- **Edad:** {age}
- **Peso:** {weight}
- **Raza:** {breed}
- **Notas:** {notes}
"""

        care_btn.click(
            fn=build_pet_profile,
            inputs=[care_name, care_type, care_age, care_weight, care_breed, care_notes],
            outputs=care_output
        )

    # =========================
    # PAWTRACK
    # =========================
    with gr.Tab("PawTrack"):
        gr.Markdown("## Seguimiento diario de la mascota")

        track_food = gr.Textbox(label="Comida", placeholder="Ejemplo: 2 veces al día")
        track_water = gr.Textbox(label="Agua", placeholder="Ejemplo: normal / poca / mucha")
        track_sleep = gr.Textbox(label="Sueño", placeholder="Ejemplo: 12 horas")
        track_walk = gr.Textbox(label="Paseo / actividad", placeholder="Ejemplo: 30 minutos")
        track_mood = gr.Textbox(label="Estado general", placeholder="Ejemplo: tranquilo, activo, nervioso")
        track_notes = gr.Textbox(label="Notas del día", lines=4, placeholder="Observaciones adicionales...")

        track_btn = gr.Button("Mostrar seguimiento")
        track_output = gr.Markdown()

        def build_track_summary(food, water, sleep, walk, mood, notes):
            return f"""
## Seguimiento diario
- **Comida:** {food}
- **Agua:** {water}
- **Sueño:** {sleep}
- **Actividad:** {walk}
- **Estado general:** {mood}
- **Notas:** {notes}
"""

        track_btn.click(
            fn=build_track_summary,
            inputs=[track_food, track_water, track_sleep, track_walk, track_mood, track_notes],
            outputs=track_output
        )

    # =========================
    # PAWMEMO
    # =========================
    with gr.Tab("PawMemo"):
        gr.Markdown("## Memoria y observaciones")
        gr.Markdown("Anota momentos especiales, comportamientos curiosos o recuerdos importantes.")

        memo_title = gr.Textbox(label="Título", placeholder="Ejemplo: Primer paseo al parque")
        memo_date = gr.Textbox(label="Fecha", placeholder="Ejemplo: 27/03/2026")
        memo_text = gr.Textbox(label="Memoria", lines=8, placeholder="Escribe aquí lo que quieras recordar...")
        memo_btn = gr.Button("Mostrar memoria")
        memo_output = gr.Markdown()

        def build_memory_note(title, date, text):
            return f"""
## PawMemo
- **Título:** {title}
- **Fecha:** {date}

### Nota
{text}
"""

        memo_btn.click(
            fn=build_memory_note,
            inputs=[memo_title, memo_date, memo_text],
            outputs=memo_output
        )

demo.launch()


