import streamlit as st
import tweepy
from textblob import TextBlob

st.title('Real-Time Brand Sentiment Analysis')

# Authentication credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up authentication
client = tweepy.Client(
    bearer_token="YOUR_BEARER_TOKEN", 
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
    except Exception as e:
        st.write(f"Error fetching tweets: {str(e)}")
        return 0, 0, 0

# Input field to enter brand or hashtag
query = st.text_input("Enter a brand name or hashtag:")

if query:
    pos, neg, neut = fetch_tweets(query)
    st.write(f"Positive: {pos}, Negative: {neg}, Neutral: {neut}")
import streamlit as st
import tweepy
from textblob import TextBlob

st.title('Real-Time Brand Sentiment Analysis')

# Authentication credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up authentication
client = tweepy.Client(
    bearer_token="YOUR_BEARER_TOKEN", 
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
    except Exception as e:
        st.write(f"Error fetching tweets: {str(e)}")
        return 0, 0, 0

# Input field to enter brand or hashtag
query = st.text_input("Enter a brand name or hashtag:")

if query:
    pos, neg, neut = fetch_tweets(query)
    st.write(f"Positive: {pos}, Negative: {neg}, Neutral: {neut}")
import streamlit as st
import tweepy
from textblob import TextBlob

st.title('Real-Time Brand Sentiment Analysis')

# Authentication credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up authentication
client = tweepy.Client(
    bearer_token="YOUR_BEARER_TOKEN", 
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
    except Exception as e:
        st.write(f"Error fetching tweets: {str(e)}")
        return 0, 0, 0

# Input field to enter brand or hashtag
query = st.text_input("Enter a brand name or hashtag:")

if query:
    pos, neg, neut = fetch_tweets(query)
    st.write(f"Positive: {pos}, Negative: {neg}, Neutral: {neut}")
