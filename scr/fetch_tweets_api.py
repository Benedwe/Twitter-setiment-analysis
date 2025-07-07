import tweepy
import pandas as pd
from textblob import TextBlob

API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def fetch_tweets(query, count=10, include_retweets=False):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count)
    
    tweet_data = []
    for tweet in tweets:
        if not include_retweets and hasattr(tweet, "retweeted_status"):
            continue
        text = tweet.full_text.replace('\n', ' ')
        sentiment = analyze_sentiment(text)
        tweet_data.append({
            "tweet_id": tweet.id,
            "username": tweet.user.screen_name,
            "text": text,
            "sentiment": sentiment
        })
    return pd.DataFrame(tweet_data)

if __name__ == "__main__":
    df = fetch_tweets("twitter", count=20, include_retweets=False)
    df.to_csv("../data/raw_tweets.csv", index=False)
    print("Fetched tweets with sentiment saved to data/raw_tweets.csv")