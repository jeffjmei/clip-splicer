import subprocess
import os

def extract_clips(video_path, segments, output_dir="clips"):
    """
    Extracts clips from a video using ffmpeg based on given start and end times.

    Parameters:
        video_path (str): Path to the input video file.
        segments (list of dict): Each dict must contain 'start' and 'end' keys (in seconds).
        output_dir (str): Directory to save the extracted clips.
    """
    os.makedirs(output_dir, exist_ok=True)

    for i, seg in enumerate(segments):
        start = seg['start']
        end = seg['end']
        duration = end - start
        output_file = os.path.join(output_dir, f"clip_{i}_{int(start)}s_to_{int(end)}s.mp4")

        cmd = [
            "ffmpeg",
            "-ss", str(start),           # start time
            "-i", video_path,            # input file
            "-t", str(duration),         # duration
            "-c:v", "libx264",           # video codec
            "-c:a", "aac",               # audio codec
            "-strict", "experimental",   # allow experimental codecs if needed
            "-y",                        # overwrite output if exists
            output_file
        ]

        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
