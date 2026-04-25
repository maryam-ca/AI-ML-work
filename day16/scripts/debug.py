from app.retrieval import dual_query_search

queries = ["qdrant kia karta he", "docker compose kia krta he"]

for q in queries:
    result = dual_query_search(q)

    print("Original:", result["original_query"])
    print("Normalized:", result["normalized_query"])
    print("Results:", result["results"])
    print("=" * 50)
