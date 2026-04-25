from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

bots = {
    "A": "I believe AI and crypto will solve all human problems. I am highly optimistic about technology.",
    "B": "I believe tech companies and capitalism are harming society. I am critical of AI and big corporations.",
    "C": "I care only about markets, finance, trading, and ROI. I analyze everything financially."
}

bot_ids = list(bots.keys())
bot_embeddings = model.encode(list(bots.values()))

def route_post_to_bots(post_content, threshold=0.4):
    post_vec = model.encode([post_content])

    # cosine similarity
    post_vec = post_vec / np.linalg.norm(post_vec)
    bot_vecs = bot_embeddings / np.linalg.norm(bot_embeddings, axis=1, keepdims=True)

    similarities = np.dot(bot_vecs, post_vec.T).flatten()

    matched = []

    for i, score in enumerate(similarities):
        if score > threshold:
            matched.append(bot_ids[i])

    # fallback
    if not matched:
        matched.append(bot_ids[np.argmax(similarities)])

    return matched