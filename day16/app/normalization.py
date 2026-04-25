ROMAN_URDU_REPLACEMENTS = {
    "kia": "kya",
    "kr": "kar",
    "krta": "karta",
    "krna": "karna",
    "he": "hai",
    "hy": "hai",
    "muje": "mujhe",
    "mjhe": "mujhe",
}


def normalize_roman_urdu(text: str) -> str:
    text = text.lower().strip()
    words = text.split()

    result = []
    for w in words:
        result.append(ROMAN_URDU_REPLACEMENTS.get(w, w))

    return " ".join(result)
