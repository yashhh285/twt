import streamlit as st
import tweepy
from textblob import TextBlob

# Streamlit app title
st.title('Real-Time Brand Sentiment Analysis')

# Authentication credentials
consumer_key = '1NPBrF4NCv6yWs8W2F7rghvKo'
consumer_secret = 'lwXiDqLdrfDJ6Ds22Fg6sbrxB0WarvUy6gc35o5uIPMZECdvsR'
access_token = '1888768047424389120-zmWNFaYzLAf8NpC0Cx2sCxwNnduFjh'
access_token_secret = 'anb4sQEfG3tYJYhjfzGa8ukm71WoJfPrRFNmJFCLYA2df'

# Set up authentication
client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAMXXywEAAAAAER6jKMv2LkBrbeozon7KqTSK4XU%3DVs7K9LhTtch1pFQWB52u8hAnTzDdFdqQinaCZ1z4nIxz9CkAqp", 
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

# Input field to enter brand or hashtag (with a unique key)
query = st.text_input("Enter a brand name or hashtag:", key="brand_input")

# When the user inputs a query
if query:
    pos, neg, neut = fetch_tweets(query)
    st.write(f"Positive: {pos}, Negative: {neg}, Neutral: {neut}")

