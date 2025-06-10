import json
import pickle
import faiss # type: ignore
import os
from tqdm import tqdm # type: ignore
from sentence_transformers import SentenceTransformer # type: ignore

# Correct paths relative to project root
DATA_PATH = "data/HealthCareMagic-100k.jsonl"
INDEX_OUTPUT_PATH = "vector_store/faiss_index.pkl"

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read JSONL and create corpus
corpus = []
metadata = []

with open(DATA_PATH, "r") as f:
    for line in tqdm(f, desc="Reading data"):
        line = line.strip()
        if not line:
            continue
        item = json.loads(line)
        query = item.get("input", "").strip()
        response = item.get("output", "").strip()
        if query and response:
            combined = f"Q: {query}\nA: {response}"
            corpus.append(combined)
            metadata.append({"input": query, "output": response})

if not corpus:
    print("⚠️ No valid data found. Please check the JSONL file format.")
    exit()

print(f"✅ Total valid Q&A examples: {len(corpus)}")
print("🔍 Generating embeddings...")
embeddings = model.encode(corpus, show_progress_bar=True, normalize_embeddings=True)

index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)

with open(INDEX_OUTPUT_PATH, "wb") as f:
    pickle.dump((index, metadata), f)

print(f"✅ FAISS index saved to {INDEX_OUTPUT_PATH}")
