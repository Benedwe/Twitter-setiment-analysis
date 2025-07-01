import tweepy
import pandas as pd

API_KEY = "ScHSyI6aBQUA0l3Viyr7ZuErX"
API_SECRET = "4htKpyR04caGfJWTkFxccb9PrT9xsqNJX0UB12b0FM7aX3zAcy"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

def fetch_tweets(query, count=10):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count)
    
    tweet_data = []
    for tweet in tweets:
        tweet_data.append({
            "tweet_id": tweet.id,
            "username": tweet.user.screen_name,
            "text": tweet.full_text.replace('\n', ' '),
            "sentiment": ""  
        })
    return pd.DataFrame(tweet_data)

if __name__ == "__main__":
    df = fetch_tweets("twitter", count=20)
    df.to_csv("../data/raw_tweets.csv", index=False)
    print("Fetched tweets saved to data/raw_tweets.csv")