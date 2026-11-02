def calculate_total(amounts: list[float]) -> float:
    total = 0.0
    for amount in amounts:
        total += amount
        return total

def get_username(user_id: int) -> str | None:
    if user_id == 1:
        return "Tom"

    return None

def filter_passed(scores: list[int]) -> list[int]:
    return  [score for score in scores if score >= 60]

