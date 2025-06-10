import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model and FAISS index
model = SentenceTransformer('all-MiniLM-L6-v2')

with open("vector_store/faiss_index.pkl", "rb") as f:
    index, metadata = pickle.load(f)

def retrieve_similar_cases(query: str, top_k: int = 3):
    # Embed the query
    query_embedding = model.encode([query], normalize_embeddings=True).astype("float32")

    # Search index
    D, I = index.search(query_embedding, top_k)

    similarities = 1 - D[0]  # Cosine similarity = 1 - distance (if index is cosine-based)

    results = []
    for idx in I[0]:
        if idx < len(metadata):
            results.append(metadata[idx])

    avg_similarity = float(np.mean(similarities))

    return results, avg_similarity

# Debug/test
if __name__ == "__main__":
    query = "I feel dizzy and nauseous when standing up, but feel fine when lying down"
    results, avg_sim = retrieve_similar_cases(query)
    print(f"\nAverage similarity: {avg_sim:.4f}")
    for i, res in enumerate(results, 1):
        print(f"\nTop {i}")
        print("Q:", res["input"])
        print("A:", res["output"])
