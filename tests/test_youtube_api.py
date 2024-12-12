import pytest
from app.youtube_api import fetch_youtube_data

def test_fetch_youtube_data():
    api_key = "test-api-key"  # Replace with a valid test key
    channel_id = "test-channel-id"  # Replace with a valid test ID

    try:
        channel_data, videos_df = fetch_youtube_data(api_key, channel_id)
        assert "items" in channel_data
        assert not videos_df.empty
    except Exception as e:
        pytest.fail(f"API test failed: {e}")
