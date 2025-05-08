# Clip Splicer
Clip Splicer is a tool that automatically downloads, transcribes, and extracts topic-relevant clips from long-form video content (like YouTube videos or local recordings). It uses OpenAI’s `whisper` for transcription and semantic search via transformer embeddings to identify meaningful moments.

## Overview
1. download YouTube video from url
2. transcribe video using OpenAI `whisper`
3. identifies relevant clips
4. cuts and outputs clips

## Demo

```bash 
python3 main.py --url "https://www.youtube.com/..." --topic "your-topic"
```

```bash
python main.py --video "downloads/my_video.mp4" --topic "machine learning"
```
