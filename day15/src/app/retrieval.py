def search_chunks(query: str, limit: int):
    return [
        {
            "score": 0.9,
            "doc_id": "doc1",
            "chunk_id": "chunk1",
            "title": "Qdrant Info",
            "language": "en",
            "source": "manual",
            "chunk_index": 1,
            "text": "Qdrant stores embeddings and performs similarity search.",
        }
    ]
