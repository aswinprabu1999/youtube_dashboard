import streamlit as st
import pandas as pd
from youtube_api import fetch_youtube_data
from visualizations import create_bar_chart, create_line_chart
from PIL import Image



st.set_page_config(page_title="YouTube Data Dashboard", layout="wide")

# App Title
st.title("YouTube Data Dashboard")




# Input Fields
api_key = st.text_input("Enter YouTube API Key:", type="password")
channel_id = st.text_input("Enter YouTube Channel ID:")

# Fetch and Display Data
if api_key and channel_id:
    try:
        channel_data, videos_df = fetch_youtube_data(api_key, channel_id)

        # Channel Statistics
        st.header("Channel Statistics")
        stats = channel_data["items"][0]["statistics"]
        st.write({
            "Title": channel_data["items"][0]["snippet"]["title"],
            "Subscribers": stats["subscriberCount"],
            "Total Views": stats["viewCount"],
            "Total Videos": stats["videoCount"],
        })

        # Video Metrics
        st.header("Video Metrics")
        top_videos = videos_df.sort_values("Views", ascending=False).head(10)
        fig = create_bar_chart(top_videos, x_col="Title", y_col="Views", title="Top 10 Videos by Views")
        st.plotly_chart(fig)

        # Subscriber Trends (Placeholder)
        st.subheader("Subscriber Trends")
        trend_data = pd.DataFrame({"Subscribers": [100, 200, 300, 400, 500]})  # Replace with actual data
        trend_chart = create_line_chart(trend_data, title="Subscriber Growth")
        st.plotly_chart(trend_chart)

        # Explore Data
        st.header("Explore Video Data")
        metric = st.selectbox("Select Metric to Explore:", ["Views", "Likes", "Comments"])
        filtered_df = videos_df.sort_values(metric, ascending=False)
        st.dataframe(filtered_df)

    except Exception as e:
        st.error(f"Error: {e}")
