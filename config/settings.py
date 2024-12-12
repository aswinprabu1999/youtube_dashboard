
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
DEFAULT_CHANNEL_ID = os.getenv("DEFAULT_CHANNEL_ID", "")
