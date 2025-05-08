from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def detect_topic(segments, topic_prompt):
    timestamps = []
    for segment in segments:
        score = util.cos_sim(
            model.encode(segment['text'], convert_to_tensor=True),
            model.encode(topic_prompt, convert_to_tensor=True)
        ).item()
        if score > 0.5:
            timestamps.append((segment['start'], segment['end']))
    return timestamps
