def score_text_etaoin_shrdlu(text: str) -> int:
    frequency_table = {
        'E': 12,
        'T': 11,
        'A': 10,
        'O': 9,
        'I': 8,
        'N': 7,
        ' ': 6,
        'S': 5,
        'H': 4,
        'R': 3,
        'D': 2,
        'L': 1,
        'U': 0
    }
    score = 0
    for char in text.upper():
        score += frequency_table.get(char, 0)
    return score
