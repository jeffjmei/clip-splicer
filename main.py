import argparse
import os
from utils.transcriber import transcribe_video
from utils.topic_detector import detect_topic
from utils.clipper import extract_clips
from utils.video_loader import load_video

def main(video_url, topic_prompt):
    output_dir = "downloads"
    filename = "downloaded_video"
    clip_output_dir = "clips"

    # Download video
    video_path = os.path.join(output_dir, filename + ".mp4")
    load_video(video_url, output_dir, filename)

    # Transcribe, detect topic, and extract clips
    text, segments = transcribe_video(video_path)
    timestamps = detect_topic(segments, topic_prompt)
    extract_clips(video_path, timestamps, clip_output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="YouTube video URL")
    parser.add_argument("--topic", required=True, help="Topic prompt to search for")
    args = parser.parse_args()

    main(args.url, args.topic)
