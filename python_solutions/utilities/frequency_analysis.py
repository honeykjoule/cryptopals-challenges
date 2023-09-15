def score_text(text: str, frequency_table: dict) -> int:
    score = 0
    for char in text.upper():
        score += frequency_table.get(char, 0)
    return score
