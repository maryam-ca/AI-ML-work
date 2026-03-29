from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, List, Dict

from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
COLLECTION_NAME = "week2_day12_docs"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data/day12_documents.json"
CACHE_DIR = BASE_DIR / ".cache/embeddings"
CACHE_FILE = CACHE_DIR / "day12_embedding_cache.json"
HF_CACHE_DIR = BASE_DIR / ".cache/huggingface"

QDRANT_URL = os.getenv("QDRANT_URL", "http://127.0.0.1:6333")


# 🔹 Generate unique hash for text
def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# 🔹 Load cache from file
def load_embedding_cache() -> Dict[str, List[float]]:
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    return {}


# 🔹 Save cache
def save_embedding_cache(cache: Dict[str, List[float]]) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


# 🔹 Load documents
def load_documents() -> List[Dict[str, Any]]:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


# 🔹 Load model with local cache
def get_model() -> SentenceTransformer:
    os.environ.setdefault("HF_HOME", str(HF_CACHE_DIR.resolve()))
    return SentenceTransformer(MODEL_NAME)


# 🔹 Compute or reuse embeddings
def get_or_compute_embeddings(
    model: SentenceTransformer,
    documents: List[Dict[str, Any]],
) -> List[List[float]]:
    cache = load_embedding_cache()
    vectors: List[List[float]] = []

    for doc in documents:
        text = doc["text"]
        key = sha256_text(text)

        if key in cache:
            vector = cache[key]
        else:
            vector = model.encode(text, normalize_embeddings=True).tolist()
            cache[key] = vector

        vectors.append(vector)

    save_embedding_cache(cache)
    return vectors


# 🔹 Create collection
def recreate_collection(client: QdrantClient, vector_size: int) -> None:
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE,
        ),
    )


# 🔹 Insert documents into Qdrant
def upsert_documents(
    client: QdrantClient,
    documents: List[Dict[str, Any]],
    vectors: List[List[float]],
) -> None:
    points: List[models.PointStruct] = []

    for idx, (doc, vector) in enumerate(
        zip(documents, vectors, strict=False), start=1
    ):
        points.append(
            models.PointStruct(
                id=idx,
                vector=vector,
                payload=doc,
            )
        )

    client.upsert(collection_name=COLLECTION_NAME, points=points)


# 🔹 Perform semantic search
def run_search(
    client: QdrantClient,
    model: SentenceTransformer,
    query: str,
) -> None:
    query_vector = model.encode(query, normalize_embeddings=True).tolist()

    hits = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3,
        with_payload=True,
    )

    print(f"\nQuery: {query}")
    for point in hits.points:
        print(point.payload)


# 🔹 Main pipeline
def main() -> None:
    documents = load_documents()
    model = get_model()

    vectors = get_or_compute_embeddings(model, documents)

    if not vectors:
        raise RuntimeError("No vectors generated!")

    client = QdrantClient(url=QDRANT_URL)

    recreate_collection(client, len(vectors[0]))
    upsert_documents(client, documents, vectors)

    print("Documents uploaded successfully!")

    run_search(client, model, "How to build APIs?")
    run_search(client, model, "ویکٹر سرچ کیا ہے؟")


if __name__ == "__main__":
    main()