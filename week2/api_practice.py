import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 999
}

try:
    response = requests.get(
        url,
        params= params, 
        timeout= 10,
    )
    response.raise_for_status()
    data = response.json()

    def extract_titles(posts):
        return [post["title"] for post in posts]

    def test_extract_titles():
        posts = [
            {"title": "Python"},
            {"title": "Agent"}
        ]

        assert extract_titles(posts) == [
            "Python",
            "Agent"
        ]

    print("========== Article Search ==========")
    
    print(f"\nUser ID: {params['userId']}\n")
    
    print(f"\nFound articles: {len(data)}\n")
    
    for index, post in enumerate(data, start=1):
        print(f"{index}. {post['title']}")

except requests.exceptions.Timeout:
    print("请求超时")

except requests.exceptions.HTTPError as e:
    print("HTTP错误:", e)

except requests.exceptions.RequestException as e:
    print("网络请求失败:", e)

except ValueError:
    print("JSON解析失败")


