"""
Twitter API helper using tweepy.Client (v2).
Requires BEARER_TOKEN in environment.
"""
import os
import tweepy
import pandas as pd
from typing import Optional
from dotenv import load_dotenv
import logging
load_dotenv()

LOGGER = logging.getLogger(__name__)

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

if not BEARER_TOKEN:
    LOGGER.warning("TWITTER_BEARER_TOKEN not set in env. get_tweets will fail without it.")

def get_tweets(keyword: str, max_results: int = 50, expansions: Optional[list]=None) -> pd.DataFrame:
    """
    Fetch recent tweets containing `keyword`. Excludes retweets, English only by default.
    Returns pandas DataFrame with columns: created_at, id, text.
    """
    if not BEARER_TOKEN:
        raise ValueError("Twitter BEARER_TOKEN not set in .env")

    client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)
    # Basic query: keyword, exclude retweets, English
    query = f"{keyword} -is:retweet lang:en"

    # tweepy Client.search_recent_tweets returns up to 100 per request
    max_pages = 1
    # limit max_results to 100 per call (Twitter API limit)
    total = min(max_results, 100)
    LOGGER.info(f"Searching tweets for: {keyword} (count={total})")

    resp = client.search_recent_tweets(query=query, max_results=total, tweet_fields=["created_at","lang","public_metrics"])
    rows = []
    if resp and resp.data:
        for t in resp.data:
            rows.append({
                "id": t.id,
                "created_at": t.created_at,
                "text": t.text
            })
    df = pd.DataFrame(rows)
    return df
