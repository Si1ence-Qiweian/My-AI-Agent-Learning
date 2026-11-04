from .services import count_articles

def display_articles(posts: list[dict], user_id: int) -> None:
    print("========== Article Search ==========")
    print(f"\nUser ID: {user_id}")
    print(f"\nFound articles: {count_articles(posts)}\n")
    
    for index, post in enumerate(posts, start=1):
        print(f"{index}. Title: {post['title']}")
        print(f"   Body: {post['body'][:80]}\n")

    print("=======================================")