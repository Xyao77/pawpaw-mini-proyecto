import os
import uuid
import subprocess


def merge_video_and_audio(video_path, audio_path, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"merged_{uuid.uuid4().hex[:8]}.mp4")

    command = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-i", audio_path,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "23",
        "-r", "24",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-shortest",
        output_path
    ]

    subprocess.run(command, check=True)

    return output_path