from .api_client import configure_logging,fetch_articles
import argparse
from .utils import display_articles

parser = argparse.ArgumentParser(description="Article Explorer")
parser.add_argument(
    '--user-id',
    help="用户 ID",
    default= 1,
    type= int,
)
args = parser.parse_args()

def main():
    configure_logging()
    if args.user_id <= 0:
        parser.error("--user-id 必须是正整数")

    articles = fetch_articles(args.user_id)
    display_articles(articles, args.user_id)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
