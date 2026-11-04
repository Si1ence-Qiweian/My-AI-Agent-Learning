from fastapi import FastAPI

app = FastAPI()

@app.get("/articles")
def get_articles(user_id: int = 1):
    return {
        "user_id": user_id,
        "articles": []
    }