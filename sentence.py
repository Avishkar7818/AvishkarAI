import os
import re
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle

text_folder = r"D:\AvishkarAI\PDFs\parsed_text"
embedding_folder = r"D:\AvishkarAI\PDFs\embeddings_folder"
os.makedirs(embedding_folder, exist_ok=True)

# Load embedding model (MPNet is great for semantic tasks)
model = SentenceTransformer('all-mpnet-base-v2')

def clean_text(text):
    # Basic cleaning: remove multiple spaces, newlines
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_into_chunks(text, max_words=150):
    words = text.split()
    return [' '.join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

for filename in os.listdir(text_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(text_folder, filename), 'r', encoding='utf-8') as f:
            text = f.read()

        cleaned = clean_text(text)
        chunks = split_into_chunks(cleaned, max_words=150)

        # Generate embeddings
        embeddings = model.encode(chunks)

        # Save embeddings and chunks as a .pkl file
        data = {
            "chunks": chunks,
            "embeddings": embeddings
        }

        base_name = filename.replace(".txt", ".pkl")
        with open(os.path.join(embedding_folder, base_name), 'wb') as out_file:
            pickle.dump(data, out_file)

        print(f"✅ Processed and saved: {filename}")
