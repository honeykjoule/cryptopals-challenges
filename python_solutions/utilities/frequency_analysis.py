def generate_frequency_table() -> dict:
    table = {}
    for index, char in enumerate('ETAOIN SHRDLU'):
        table[char] = 12 - index
    return table

def score_text(text: str, frequency_table: dict) -> int:
    score = 0
    for char in text.upper():
        score += frequency_table.get(char, 0)
    return score
