import argparse
import os
from utils.transcriber import transcribe_video
from utils.topic_detector import detect_topic
from utils.clipper import extract_clips
from utils.video_loader import load_video

def main(video_path, topic_prompt, is_downloaded=False, video_url=None):
    output_dir = "downloads"
    filename = "downloaded_video"
    clip_output_dir = "clips"

    # If not using local file, download from URL
    if not is_downloaded and video_url:
        video_path = os.path.join(output_dir, filename + ".mp4")
        load_video(video_url, output_dir, filename)

    print(f"Processing: {video_path}")
    text, segments = transcribe_video(video_path)
    timestamps = detect_topic(segments, topic_prompt)
    extract_clips(video_path, timestamps, clip_output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="YouTube URL to download and process")
    group.add_argument("--video", help="Path to a local video file to process")

    parser.add_argument("--topic", required=True, help="Topic prompt to search for")
    args = parser.parse_args()

    # Decide mode based on which arg was used
    if args.video:
        main(args.video, args.topic, is_downloaded=True)
    else:
        main(None, args.topic, is_downloaded=False, video_url=args.url)
