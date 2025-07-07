import pandas as pd

class TweetFetcher:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def fetch_tweets(self, n=5):
        df = pd.read_csv(self.csv_path)
        return df.head(n)

if __name__ == "__main__":
    fetcher = TweetFetcher("data/raw_tweets.csv")
    tweets = fetcher.fetch_tweets(5)
    print(tweets[['tweet_id', 'text']])
    df = pd.read_csv('data/raw_tweets.csv')
df.to_json('scr/raw_tweets.json', orient='records')