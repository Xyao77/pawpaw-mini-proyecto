import os
import uuid
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def find_font_paths():
    """
    Return one font for Chinese-friendly rendering and one for Latin text.
    """
    zh_candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc"
    ]

    latin_candidates = [
        "/System/Library/Fonts/Supplemental/Avenir Next.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica.ttc"
    ]

    zh_font = None
    latin_font = None

    for path in zh_candidates:
        if os.path.exists(path):
            zh_font = path
            break

    for path in latin_candidates:
        if os.path.exists(path):
            latin_font = path
            break

    if zh_font is None:
        zh_font = latin_font
    if latin_font is None:
        latin_font = zh_font

    return zh_font, latin_font


def contains_chinese(text):
    return any('\u4e00' <= ch <= '\u9fff' for ch in text)


def get_font(font_size, text):
    zh_font_path, latin_font_path = find_font_paths()
    chosen_path = zh_font_path if contains_chinese(text) else latin_font_path

    if chosen_path is None:
        raise ValueError("No suitable font file found.")

    return ImageFont.truetype(chosen_path, font_size)


def draw_text_with_shadow(draw, position, text, font, fill, shadow_fill):
    x, y = position
    offsets = [(-2, -2), (2, -2), (-2, 2), (2, 2), (0, 2), (2, 0)]

    for dx, dy in offsets:
        draw.text((x + dx, y + dy), text, font=font, fill=shadow_fill)

    draw.text((x, y), text, font=font, fill=fill)


def wrap_text(draw, text, font, max_width):
    # Chinese: char by char
    if contains_chinese(text):
        units = list(text)
        joiner = ""
    else:
        units = text.split()
        joiner = " "

    lines = []
    current = ""

    for unit in units:
        test_line = current + unit if joiner == "" else (current + joiner + unit).strip()
        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_width = bbox[2] - bbox[0]

        if line_width <= max_width:
            current = test_line
        else:
            if current:
                lines.append(current)
            current = unit

    if current:
        lines.append(current)

    return lines


def add_subtitle_to_video(video_path, hook_text, main_text, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"subtitled_{uuid.uuid4().hex[:8]}.mp4")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Could not open input video.")

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 24

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Smaller hook font, bigger main font
    hook_font = get_font(32, hook_text)
    main_font = get_font(54, main_text)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(frame_rgb).convert("RGBA")
        draw = ImageDraw.Draw(pil_img)

        # ---------- TOP HOOK ----------
        hook_lines = wrap_text(draw, hook_text, hook_font, int(width * 0.68))
        hook_line_height = 34

        # move hook lower than before
        hook_start_y = int(height * 0.22)

        for i, line in enumerate(hook_lines):
            bbox = draw.textbbox((0, 0), line, font=hook_font)
            line_width = bbox[2] - bbox[0]
            x = (width - line_width) // 2
            y = hook_start_y + i * hook_line_height

            draw_text_with_shadow(
                draw,
                (x, y),
                line,
                hook_font,
                fill=(245, 245, 245, 230),
                shadow_fill=(0, 0, 0, 180)
            )

        # ---------- MAIN TEXT ----------
        main_lines = wrap_text(draw, main_text, main_font, int(width * 0.72))
        main_line_height = 68

        total_main_height = len(main_lines) * main_line_height

        # move main text upward, more like content title
        main_start_y = int(height * 0.76) - total_main_height // 2

        for i, line in enumerate(main_lines):
            bbox = draw.textbbox((0, 0), line, font=main_font)
            line_width = bbox[2] - bbox[0]
            x = (width - line_width) // 2
            y = main_start_y + i * main_line_height

            draw_text_with_shadow(
                draw,
                (x, y),
                line,
                main_font,
                fill=(255, 248, 235, 255),   # warm white
                shadow_fill=(0, 0, 0, 235)
            )

        final_frame = cv2.cvtColor(np.array(pil_img.convert("RGB")), cv2.COLOR_RGB2BGR)
        out.write(final_frame)

    cap.release()
    out.release()

    return output_path