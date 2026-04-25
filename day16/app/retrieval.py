from .data import DATA
from .normalization import normalize_roman_urdu


#  search function
def search_chunks(query):
    results = []
    query_words = query.lower().split()

    for item in DATA:
        text = item["text"].lower()
        score = 0

        for word in query_words:
            if word in text:
                score += 1

        if score > 0:
            results.append(
                {"chunk_id": item["chunk_id"], "text": item["text"], "score": score}
            )

    return results


#  merge results
def merge_results(r1, r2):
    merged = {item["chunk_id"]: item for item in r1}

    for item in r2:
        if item["chunk_id"] not in merged:
            merged[item["chunk_id"]] = item

    return list(merged.values())


#  MAIN FUNCTION
def dual_query_search(query):
    original_query = query
    normalized_query = normalize_roman_urdu(query)

    # dono queries run karo
    results_original = search_chunks(original_query)
    results_normalized = search_chunks(normalized_query)

    # merge karo
    merged = merge_results(results_original, results_normalized)

    return {
        "original_query": original_query,
        "normalized_query": normalized_query,
        "results": merged,
    }
