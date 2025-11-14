import streamlit as st
import tweepy
import pandas as pd

# ------------------------
# 1. Twitter API setup
# ------------------------
bearer_token = "YOUR_BEARER_TOKEN"

client = tweepy.Client(
    bearer_token=bearer_token,
    wait_on_rate_limit=True
)

# ------------------------
# 2. Function to fetch tweets
# ------------------------
def fetch_tweets(query, max_results=10):
    tweets = client.search_recent_tweets(
        query=f"{query} -is:retweet lang:en",
        max_results=max_results,
        tweet_fields=["created_at", "text", "author_id"]
    )

    data = []
    if tweets.data:
        for t in tweets.data:
            data.append({
                "created_at": t.created_at,
                "author_id": t.author_id,
                "text": t.text
            })

    return pd.DataFrame(data)


# ------------------------
# 3. Streamlit UI
# ------------------------
st.title("🔍 Twitter Search App")
st.write("Search any topic and view recent tweets.")

# Input box
keyword = st.text_input("Enter topic keyword", "Python")

# Search button
if st.button("Search Tweets"):
    if keyword.strip() == "":
        st.warning("Keyword can't be empty.")
    else:
        st.write("Fetching tweets...")
        df = fetch_tweets(keyword, max_results=10)

        if df.empty:
            st.error("No tweets found.")
        else:
            st.success("Here are your tweets:")
            st.dataframe(df)
