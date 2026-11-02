import argparse
import logging
from collections.abc import Sequence

import requests

try:
    from .config import API_BASE_URL, TIMEOUT
except ImportError:
    from config import API_BASE_URL, TIMEOUT


logger = logging.getLogger(__name__)


def extract_titles(posts: list[dict]) -> list[str]:
    return [post["title"] for post in posts]


def fetch_articles(user_id: int) -> list[dict]:
    if not API_BASE_URL:
        logger.error("未配置 API_BASE_URL")
        return []

    try:
        logger.info("开始请求 API，用户 ID: %s", user_id)
        response = requests.get(
            API_BASE_URL,
            params={"userId": user_id},
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, list) or not all(
            isinstance(post, dict) for post in data
        ):
            raise ValueError("API 返回的数据不是文章列表")

        return data
    except requests.exceptions.Timeout:
        logger.warning("请求超时")
    except requests.exceptions.HTTPError as error:
        logger.error("HTTP 错误: %s", error)
    except requests.exceptions.RequestException as error:
        logger.error("网络请求失败: %s", error)
    except (requests.exceptions.JSONDecodeError, ValueError) as error:
        logger.error("响应解析失败: %s", error)

    return []


def display_articles(posts: list[dict], user_id: int) -> None:
    titles = extract_titles(posts)

    print("========== Article Search ==========")
    print(f"\nUser ID: {user_id}")
    print(f"\nFound articles: {len(titles)}\n")

    for index, title in enumerate(titles, start=1):
        print(f"{index}. {title}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Article Search Tool")
    parser.add_argument(
        "--user-id",
        type=int,
        default=1,
        help="用户 ID（正整数）",
    )
    return parser


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="app.log",
        encoding="utf-8",
    )


def main(argv: Sequence[str] | None = None) -> int:
    configure_logging()
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.user_id <= 0:
        parser.error("--user-id 必须是正整数")

    articles = fetch_articles(args.user_id)
    display_articles(articles, args.user_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


def test_extract_titles_empty():
    assert extract_titles([]) == []
