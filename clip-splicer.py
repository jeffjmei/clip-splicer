
# ================
# Import Libraries
# ================
#from pytube import YouTube # for importing videos
#import whisper # for processing video
#from moviepy.editor import VideoFileClip, concatenate_videoclips # video editing
import subprocess # for importing videos
import whisper # for video transcription

# ===============
# Download Video 
# ===============

# Download the video to the current directory
url = 'https://www.youtube.com/watch?v=9b4OAlpPhNA' # trump interview
url = 'https://www.youtube.com/watch?v=pY23ctQYGl4' # columbia arrests
subprocess.run(['yt-dlp', url])

# Transcribe Data
model = whisper.load_model("base")  # or "small", "medium", "large" for more accuracy
result = model.transcribe("columbia-arrests.mkv")
print(result["text"])

# Print or inspect segments with timestamps
for segment in result["segments"]:
    print(f"[{segment['start']:.2f} - {segment['end']:.2f}] {segment['text']}")

# Keyword Search
keywords = ["Palestine", "Columbia"]
highlight_segments = [
    seg for seg in result["segments"]
    if any(k in seg["text"].lower() for k in keywords)
]

