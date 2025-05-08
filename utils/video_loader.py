import subprocess
import os

def load_video(url, output_dir="downloads", filename="video.mp4"):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    subprocess.run([
        'yt-dlp',
        url,
        '-o', output_path,  # Set output file path
        '--merge-output-format', 'mp4'
    ], check=True)

    return output_path


