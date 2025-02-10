import streamlit as st
import tweepy
from textblob import TextBlob

# Authentication credentials (ensure these are securely managed)
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up authentication and API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to fetch tweets and analyze sentiment
def fetch_tweets(query):
    tweets = api.search(q=query, lang='en', count=100)
    positive, negative, neutral = 0, 0, 0
    for tweet in tweets:
        blob = TextBlob(tweet.text)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            positive += 1
        elif sentiment < 0:
            negative += 1
        else:
            neutral += 1
    return positive, negative, neutral

# Streamlit UI
st.title("Real-Time Brand Sentiment Analysis")
query = st.text_input("Enter a brand name or hashtag:")
if query:
    pos, neg, neut = fetch_tweets(query)
    st.write(f"Positive Tweets: {pos}")
    st.write(f"Negative Tweets: {neg}")
    st.write(f"Neutral Tweets: {neut}")
    st.bar_chart([pos, neg, neut], use_container_width=True)
