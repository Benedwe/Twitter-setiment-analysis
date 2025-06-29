import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class SentimentVisualizer:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)

    def plot_sentiment_distribution(self, sentiment_column='sentiment'):
        plt.figure(figsize=(6,4))
        sns.countplot(data=self.df, x=sentiment_column, palette='Set2')
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Number of Tweets')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    visualizer = SentimentVisualizer("../data/raw_tweets.csv")
    visualizer.plot_sentiment_distribution()
