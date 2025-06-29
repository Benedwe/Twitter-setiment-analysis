# Twitter Sentiment Analysis

This project analyzes the sentiment of tweets using Python. It includes data preprocessing, sentiment analysis, visualization, and a Jupyter notebook for interactive exploration.

## Project Structure

```
Twitter Sentiment/
│
├── data/
│   └── raw_tweets.csv
├── scr/
│   ├── fetch_tweets.py
│   ├── preprocess.py
│   ├── sentiment.py
│   └── visualize.py
├── notebooks/
│   └── analysis.ipynb
├── requirements.txt
└── README.md
```

## Features

- **Fetch Tweets:** Load and display tweets from a CSV file.
- **Preprocessing:** Clean tweet text (remove URLs, mentions, hashtags, punctuation, numbers).
- **Sentiment Analysis:** Classify tweets as positive, negative, or neutral using TextBlob.
- **Visualization:** Plot sentiment distribution using Seaborn/Matplotlib.
- **Jupyter Notebook:** Interactive analysis and visualization.

## Getting Started

### 1. Clone the repository

```sh
git clone <repository-url>
cd Twitter\ Sentiment
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Prepare your data

Edit `data/raw_tweets.csv` with your tweet data. Example format:

```csv
tweet_id,username,text,sentiment
1,alice,"I love the new features on Twitter!",positive
2,bob,"This update is terrible. #disappointed",negative
```

### 4. Run the scripts

- **Fetch tweets:**  
  `python scr/fetch_tweets.py`

- **Preprocess tweets:**  
  `python scr/preprocess.py`

- **Analyze sentiment:**  
  `python scr/sentiment.py`

- **Visualize results:**  
  `python scr/visualize.py`

### 5. Use the Jupyter notebook

```sh
jupyter notebook notebooks/analysis.ipynb
```

## Requirements

See `requirements.txt` for all dependencies.

## License

This project is for educational purposes.