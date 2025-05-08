import whisper

model = whisper.load_model("base")

def transcribe_video(path):
    result = model.transcribe(path)
    return result['text'], result['segments']
