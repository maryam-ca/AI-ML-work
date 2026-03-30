from app.vector_store import get_qdrant_client
from sentence_transformers import SentenceTransformer

MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
COLLECTION = "day13_chunks"


def main():
    client = get_qdrant_client()
    model = SentenceTransformer(MODEL)

    query = "What is Qdrant?"
    vector = model.encode(query).tolist()

    results = client.query_points(collection_name=COLLECTION, query=vector, limit=3)

    print("\n🔍 SEARCH RESULTS:\n")

    for r in results.points:
        print("Doc ID:", r.payload.get("doc_id"))
        print("Chunk ID:", r.payload.get("chunk_id"))
        print("Text:", r.payload.get("text"))
        print("-" * 40)


if __name__ == "__main__":
    main()
