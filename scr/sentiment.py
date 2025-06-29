import pandas as pd
from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)

    def analyze_sentiment(self, text):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            return 'positive'
        elif polarity < 0:
            return 'negative'
        else:
            return 'neutral'

    def add_sentiment_column(self):
        self.df['predicted_sentiment'] = self.df['text'].apply(self.analyze_sentiment)

    def save_results(self, output_path):
        self.df.to_csv(output_path, index=False)

if __name__ == "__main__":
    analyzer = SentimentAnalyzer("../data/raw_tweets.csv")