from flask import Flask, render_template, request, jsonify, send_from_directory
from textblob import TextBlob
import pandas as pd
import json
import os

app = Flask(__name__, static_folder="scr", template_folder="scr")

@app.route("/")
def index():
    return render_template("UI.html")

@app.route("/data/<path:filename>")
def serve_data(filename):
    """Serve data files from the data directory"""
    return send_from_directory("data", filename)

@app.route("/api/tweets")
def get_tweets():
    """API endpoint to get tweets data"""
    try:
        # Try to load from CSV first
        csv_path = "data/raw_tweets.csv"
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            return jsonify(df.to_dict('records'))
        else:
            # Fallback to JSON
            json_path = "scr/raw_tweets .json"
            if os.path.exists(json_path):
                with open(json_path, 'r') as f:
                    return jsonify(json.load(f))
            else:
                return jsonify({"error": "No data files found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/tweets-with-sentiment")
def get_tweets_with_sentiment():
    """API endpoint to get tweets with predicted sentiment"""
    try:
        csv_path = "data/tweets_with_sentiment.csv"
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            return jsonify(df.to_dict('records'))
        else:
            return jsonify({"error": "No sentiment data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return jsonify({"sentiment": sentiment, "polarity": polarity})

@app.route("/api/statistics")
def get_statistics():
    """Get sentiment statistics from the data"""
    try:
        # Try to load tweets with sentiment first
        csv_path = "data/tweets_with_sentiment.csv"
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            sentiment_col = 'predicted_sentiment' if 'predicted_sentiment' in df.columns else 'sentiment'
        else:
            # Fallback to raw tweets
            csv_path = "data/raw_tweets.csv"
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                sentiment_col = 'sentiment'
            else:
                return jsonify({"error": "No data files found"}), 404
        
        # Calculate statistics
        sentiment_counts = df[sentiment_col].value_counts().to_dict()
        total_tweets = len(df)
        
        return jsonify({
            "total_tweets": total_tweets,
            "sentiment_distribution": sentiment_counts,
            "positive_percentage": (sentiment_counts.get('positive', 0) / total_tweets) * 100,
            "neutral_percentage": (sentiment_counts.get('neutral', 0) / total_tweets) * 100,
            "negative_percentage": (sentiment_counts.get('negative', 0) / total_tweets) * 100
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)