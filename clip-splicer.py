
# ================
# Import Libraries
# ================
#from pytube import YouTube # for importing videos
#import whisper # for processing video
#from moviepy.editor import VideoFileClip, concatenate_videoclips # video editing
import subprocess # for importing videos

# ===============
# Download Video 
# ===============
url = 'https://www.youtube.com/watch?v=9b4OAlpPhNA'
yt = YouTube(url)

# Download the video to the current directory
subprocess.run(['yt-dlp', url])


