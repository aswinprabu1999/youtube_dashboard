import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

# Video ID of the YouTube video
video_id = "4sZFkPw87ng"

# Initialize YouTube API client
youtube = build("youtube", "v3", developerKey=api_key)

# Make the API request
try:
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    print(response)
except Exception as e:
    print(f"Error: {e}")
