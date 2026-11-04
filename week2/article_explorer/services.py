def extract_titles(posts: list[dict]) -> list[str]:
    return [post["title"] for post in posts]

def extract_bodies(posts: list[dict]) -> list[str]:
    return [post["body"] for post in posts]

def count_articles(posts: list[dict]) -> int:
    return len(posts)