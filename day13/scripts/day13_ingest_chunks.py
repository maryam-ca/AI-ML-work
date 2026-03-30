import json
from pathlib import Path

from app.ingestion import build_chunk_records
from app.vector_store import get_qdrant_client, recreate_collection
from qdrant_client import models
from sentence_transformers import SentenceTransformer

MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
COLLECTION = "day13_chunks"
DATA = Path("data/raw/day13_documents.json")


def main():
    docs = json.loads(DATA.read_text())
    chunks = build_chunk_records(docs)

    model = SentenceTransformer(MODEL)
    vectors = model.encode([c["text"] for c in chunks]).tolist()

    client = get_qdrant_client()
    recreate_collection(client, COLLECTION, len(vectors[0]))

    points = []
    for i, (chunk, vector) in enumerate(zip(chunks, vectors, strict=False)):
        points.append(models.PointStruct(id=i, vector=vector, payload=chunk))

    client.upsert(collection_name=COLLECTION, points=points)

    print("✅ Ingestion Complete")


if __name__ == "__main__":
    main()
