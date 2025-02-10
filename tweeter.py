import streamlit as st
import tweepy
from textblob import TextBlob
import time

# Load credentials from Streamlit secrets
consumer_key = st.secrets["TWITTER_CONSUMER_KEY"]
consumer_secret = st.secrets["TWITTER_CONSUMER_SECRET"]
access_token = st.secrets["TWITTER_ACCESS_TOKEN"]
access_token_secret = st.secrets["TWITTER_ACCESS_TOKEN_SECRET"]
bearer_token = st.secrets["TWITTER_BEARER_TOKEN"]

# Set up authentication
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Function to fetch tweets and analyze sentiment
def fetch_tweets(query):
    try:
        st.write(f"Fetching tweets for: {query}")
        tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["text"])

        if tweets.data is None:
            st.write("No tweets found for this query.")
            return 0, 0, 0

        st.write(f"Found {len(tweets.data)} tweets.")
        positive, negative, neutral = 0, 0, 0

        for tweet in tweets.data:
            blob = TextBlob(tweet.text)
            sentiment = blob.sentiment.polarity
            if sentiment > 0:
                positive += 1
            elif sentiment < 0:
                negative += 1
            else:
                neutral += 1
        return positive, negative, neutral

    except tweepy.TooManyRequests:
        st.write("Rate limit reached. Sleeping for 15 minutes...")
        time.sleep(15 * 60)  # Sleep for 15 minutes before retrying
        return fetch_tweets(query)

    except Exception as e:
        st.write(f"Error fetching tweets: {str(e)}")
        return 0, 0, 0

# Input field to enter brand or hashtag (with a unique key)
query = st.text_input("Enter a brand name or hashtag:", key="brand_input")

# When the user inputs a query
if query:
    pos, neg, neut = fetch_tweets(query)
    st.write(f"Positive: {pos}, Negative: {neg}, Neutral: {neut}")
