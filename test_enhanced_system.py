#!/usr/bin/env python3
"""
Test script for the enhanced Twitter Sentiment Analysis system
"""

import pandas as pd
import json
import os

def test_data_generation():
    """Test if we have generated the enhanced dataset"""
    print("🔍 Testing Data Generation...")
    
    # Check if raw tweets CSV exists
    if os.path.exists("data/raw_tweets.csv"):
        df = pd.read_csv("data/raw_tweets.csv")
        print(f"✅ Raw tweets CSV found: {len(df)} tweets")
        print(f"   Columns: {list(df.columns)}")
        
        # Check sentiment distribution
        if 'sentiment' in df.columns:
            sentiment_counts = df['sentiment'].value_counts()
            print(f"   Sentiment distribution:")
            for sentiment, count in sentiment_counts.items():
                percentage = (count / len(df)) * 100
                print(f"     {sentiment}: {count} ({percentage:.1f}%)")
    else:
        print("❌ Raw tweets CSV not found")
    
    # Check if JSON file exists
    if os.path.exists("scr/raw_tweets.json"):
        with open("scr/raw_tweets.json", 'r') as f:
            data = json.load(f)
        print(f"✅ Raw tweets JSON found: {len(data)} tweets")
    else:
        print("❌ Raw tweets JSON not found")

def test_sentiment_analysis():
    """Test if sentiment analysis has been applied"""
    print("\n🔍 Testing Sentiment Analysis...")
    
    if os.path.exists("data/tweets_with_sentiment.csv"):
        df = pd.read_csv("data/tweets_with_sentiment.csv")
        print(f"✅ Tweets with sentiment CSV found: {len(df)} tweets")
        
        if 'predicted_sentiment' in df.columns:
            sentiment_counts = df['predicted_sentiment'].value_counts()
            print(f"   Predicted sentiment distribution:")
            for sentiment, count in sentiment_counts.items():
                percentage = (count / len(df)) * 100
                print(f"     {sentiment}: {count} ({percentage:.1f}%)")
        else:
            print("   ⚠️  No 'predicted_sentiment' column found")
    else:
        print("❌ Tweets with sentiment CSV not found")

def test_sample_tweets():
    """Display some sample tweets"""
    print("\n🔍 Sample Tweets...")
    
    if os.path.exists("data/raw_tweets.csv"):
        df = pd.read_csv("data/raw_tweets.csv")
        print("Sample tweets from the dataset:")
        for i, row in df.head(5).iterrows():
            sentiment = row.get('sentiment', 'N/A')
            username = row.get('username', 'Unknown')
            text = row.get('text', 'No text')[:100] + "..." if len(row.get('text', '')) > 100 else row.get('text', 'No text')
            print(f"   {i+1}. @{username} ({sentiment}): {text}")

def main():
    """Run all tests"""
    print("🚀 Testing Enhanced Twitter Sentiment Analysis System")
    print("=" * 60)
    
    test_data_generation()
    test_sentiment_analysis()
    test_sample_tweets()
    
    print("\n" + "=" * 60)
    print("✅ Testing completed!")
    print("\nTo start the web application:")
    print("   python app.py")
    print("\nThen open your browser to: http://localhost:5000")

if __name__ == "__main__":
    main() 