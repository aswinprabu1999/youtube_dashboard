from googleapiclient.discovery import build
import pandas as pd

def fetch_youtube_data(api_key, channel_id):
    youtube = build("youtube", "v3", developerKey=api_key)

    # Fetch channel details
    channel_request = youtube.channels().list(
        part="statistics,snippet,contentDetails", id=channel_id
    )
    channel_response = channel_request.execute()

    # Fetch uploaded videos from playlist
    playlist_id = channel_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    video_request = youtube.playlistItems().list(
        part="snippet", playlistId=playlist_id, maxResults=50
    )
    video_response = video_request.execute()

    videos = []
    for item in video_response["items"]:
        video_id = item["snippet"]["resourceId"]["videoId"]
        title = item["snippet"]["title"]

        # Fetch video statistics
        stats_request = youtube.videos().list(part="statistics", id=video_id)
        stats_response = stats_request.execute()
        stats = stats_response["items"][0]["statistics"]

        videos.append({
            "Title": title,
            "Video ID": video_id,
            "Views": int(stats.get("viewCount", 0)),
            "Likes": int(stats.get("likeCount", 0)),
            "Comments": int(stats.get("commentCount", 0)),
        })

    return channel_response, pd.DataFrame(videos)
