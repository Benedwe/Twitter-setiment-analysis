import re
import pandas as pd

class Preprocessor:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)

    @staticmethod
    def clean_text(text):
        text = text.lower()
        text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  
        text = re.sub(r'\@\w+|\#','', text) 
        text = re.sub(r'[^\w\s]', '', text) 
        text = re.sub(r'\d+', '', text)      
        text = text.strip()
        return text

    def preprocess(self):
        self.df['clean_text'] = self.df['text'].apply(self.clean_text)

    def save_clean_data(self, output_path):
        self.df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocessor = Preprocessor("../data/raw_tweets.csv")
    preprocessor.preprocess()