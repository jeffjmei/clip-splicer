from sentence_transformers import SentenceTransformer, util

# Load the embedding model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def detect_topic(segments, topic_prompt, similarity_threshold=0.5):
    """
    Identifies which transcript segments are relevant to a given topic.

    Parameters:
        segments (list of dict): Each dict must contain 'text', 'start', and 'end'.
        topic_prompt (str): The topic or phrase you're searching for.
        similarity_threshold (float): Cosine similarity threshold for topic relevance.

    Returns:
        List of matching segments with original text and timestamps.
    """
    topic_embedding = model.encode(topic_prompt, convert_to_tensor=True)
    highlight_segments = []

    for seg in segments:
        text = seg['text']
        text_embedding = model.encode(text, convert_to_tensor=True)
        similarity = util.cos_sim(topic_embedding, text_embedding).item()

        if similarity >= similarity_threshold:
            highlight_segments.append({
                'start': seg['start'],
                'end': seg['end'],
                'text': text,
                'score': round(similarity, 3)
            })

    return highlight_segments
