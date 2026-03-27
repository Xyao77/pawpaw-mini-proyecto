import os
import uuid
import subprocess


def generate_tts_audio(text, language="中文", output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    aiff_path = os.path.join(output_dir, f"tts_{uuid.uuid4().hex[:8]}.aiff")
    wav_path = aiff_path.replace(".aiff", ".wav")

    voice_map = {
        "中文": "Meijia",
        "Español": "Sandy (西班牙语（西班牙）)",
        "English": "Samantha"
    }

    selected_voice = voice_map.get(language, "Samantha")

    # Step 1: generate AIFF using macOS say
    subprocess.run([
        "say",
        "-v", selected_voice,
        "-o", aiff_path,
        text
    ], check=True)

    # Step 2: convert AIFF to WAV using ffmpeg
    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", aiff_path,
        wav_path
    ], check=True)

    return wav_path