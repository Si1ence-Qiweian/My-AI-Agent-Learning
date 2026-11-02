from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

API_BASE_URL = os.getenv("API_BASE_URL")

TIMEOUT = 10

MAX_RETRIES = 3