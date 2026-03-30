import os

from qdrant_client import QdrantClient, models

QDRANT_URL = os.getenv("QDRANT_URL", "http://127.0.0.1:6333")


def get_qdrant_client():
    return QdrantClient(url=QDRANT_URL)


def recreate_collection(client, name, vector_size):
    if client.collection_exists(name):
        client.delete_collection(name)

    client.create_collection(
        collection_name=name,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE,
        ),
    )
