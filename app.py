from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__, static_folder="scr", template_folder="scr")

@app.route("/")
def index():
    return render_template("UI.html")

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

if __name__ == "__main__":
    app.run(debug=True)