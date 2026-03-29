from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
    VectorParams,
)

COLLECTION = "week2_day11_vectors"
QDRANT_URL = "http://qdrant:6333"


def main():
    client = QdrantClient(url=QDRANT_URL)

    # Step 1: Create collection (fresh start)
    if client.collection_exists(COLLECTION):
        client.delete_collection(COLLECTION)

    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=4, distance=Distance.COSINE),
    )

    print("✅ Collection Created")

    # Step 2: Insert data
    points = [
        PointStruct(
            id=1,
            vector=[0.10, 0.20, 0.30, 0.40],
            payload={
                "doc_id": "A-001",
                "category": "notes",
                "source": "wsl",
                "score": 10,
            },
        ),
        PointStruct(
            id=2,
            vector=[0.11, 0.19, 0.29, 0.39],
            payload={
                "doc_id": "A-002",
                "category": "notes",
                "source": "github",
                "score": 9,
            },
        ),
        PointStruct(
            id=3,
            vector=[0.90, 0.10, 0.05, 0.02],
            payload={
                "doc_id": "B-001",
                "category": "todo",
                "source": "wsl",
                "score": 3,
            },
        ),
        PointStruct(
            id=4,
            vector=[0.88, 0.12, 0.04, 0.01],
            payload={
                "doc_id": "B-002",
                "category": "todo",
                "source": "slack",
                "score": 4,
            },
        ),
    ]

    client.upsert(collection_name=COLLECTION, points=points)

    print("✅ Data Inserted")

    # Step 3: Search without filter
    res = client.query_points(
        collection_name=COLLECTION,
        query=[0.10, 0.20, 0.30, 0.40],
        limit=3,
        with_payload=True,
    )

    print("\n🔍 Top 3 Results (No Filter):")
    for r in res.points:
        print(r.id, round(r.score, 4), r.payload)

    # Step 4: Filter search (ONLY todo)
    flt = Filter(must=[FieldCondition(key="category", match=MatchValue(value="todo"))])

    res2 = client.query_points(
        collection_name=COLLECTION,
        query=[0.10, 0.20, 0.30, 0.40],
        limit=10,
        with_payload=True,
        query_filter=flt,  # ✅ correct parameter
    )

    print("\n🔎 Filtered Results (category = todo):")
    for r in res2.points:
        print(r.id, round(r.score, 4), r.payload)


if __name__ == "__main__":
    main()
