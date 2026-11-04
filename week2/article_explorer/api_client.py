import requests
import logging
from .config import BASE_URL, TIMEOUT, LOG_LEVEL

logger = logging.getLogger(__name__)
def configure_logging() -> None:
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="app.log",
        encoding="utf-8"
    )

def fetch_articles(user_id: int) -> list[dict]:
    if not BASE_URL:
        logger.error("未配置 BASE_URL")
        return []

    try:
        logger.info("开始请求 API")
        response = requests.get(
            BASE_URL,
            params={"userId": user_id},
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()

        return data

    except requests.exceptions.Timeout:
        logger.warning("请求超时")
        return "请求超时"
    except requests.exceptions.HTTPError as e:
        logger.error("HTTP错误: %s", e)
        return "HTTP错误"
    except requests.exceptions.RequestException as e:
        logger.error("网络请求失败: %s", e)
        return "网络请求失败"
    except (requests.exceptions.JSONDecodeError, ValueError) as e:
        logger.error("响应解析失败: %s", e)
        return "响应解析失败"