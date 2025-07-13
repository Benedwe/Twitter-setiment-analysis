#!/usr/bin/env python3
"""
Test script to verify Twitter Sentiment Analysis functionality
"""

import pandas as pd
import json
import os
from textblob import TextBlob

def test_csv_data():
    """Test loading and processing CSV data"""
    print("=== Testing CSV Data ===")
    
    # Test raw tweets CSV
    csv_path = "data/raw_tweets.csv"
    if os.path.exists(csv_path):
        print(f"✓ Found {csv_path}")
        df = pd.read_csv(csv_path)
        print(f"  - Loaded {len(df)} tweets")
        print(f"  - Columns: {list(df.columns)}")
        
        # Check sentiment distribution
        sentiment_counts = df['sentiment'].value_counts()
        print(f"  - Sentiment distribution:")
        for sentiment, count in sentiment_counts.items():
            print(f"    {sentiment}: {count} ({count/len(df)*100:.1f}%)")
        
        # Test sentiment analysis on a few samples
        print("  - Testing sentiment analysis on sample tweets:")
        for i, row in df.head(3).iterrows():
            analysis = TextBlob(row['text'])
            polarity = analysis.sentiment.polarity
            predicted = 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'
            print(f"    Tweet {i+1}: '{row['text'][:50]}...'")
            print(f"      Actual: {row['sentiment']}, Predicted: {predicted}, Polarity: {polarity:.3f}")
    else:
        print(f"✗ {csv_path} not found")
    
    # Test tweets with sentiment CSV
    sentiment_csv_path = "data/tweets_with_sentiment.csv"
    if os.path.exists(sentiment_csv_path):
        print(f"\n✓ Found {sentiment_csv_path}")
        df_sentiment = pd.read_csv(sentiment_csv_path)
        print(f"  - Loaded {len(df_sentiment)} tweets with predictions")
        print(f"  - Columns: {list(df_sentiment.columns)}")
        
        if 'predicted_sentiment' in df_sentiment.columns:
            # Check prediction accuracy
            correct = 0
            total = 0
            for _, row in df_sentiment.iterrows():
                if pd.notna(row['sentiment']) and pd.notna(row['predicted_sentiment']):
                    if row['sentiment'].lower() == row['predicted_sentiment'].lower():
                        correct += 1
                    total += 1
            
            if total > 0:
                accuracy = correct / total * 100
                print(f"  - Prediction accuracy: {accuracy:.1f}% ({correct}/{total})")
    else:
        print(f"✗ {sentiment_csv_path} not found")

def test_json_data():
    """Test loading and processing JSON data"""
    print("\n=== Testing JSON Data ===")
    
    json_path = "scr/raw_tweets .json"
    if os.path.exists(json_path):
        print(f"✓ Found {json_path}")
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        print(f"  - Loaded {len(data)} tweets")
        print(f"  - Keys in first tweet: {list(data[0].keys())}")
        
        # Check sentiment distribution
        sentiment_counts = {}
        for tweet in data:
            sentiment = tweet['sentiment']
            sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
        
        print(f"  - Sentiment distribution:")
        for sentiment, count in sentiment_counts.items():
            print(f"    {sentiment}: {count} ({count/len(data)*100:.1f}%)")
        
        # Test sentiment analysis on a few samples
        print("  - Testing sentiment analysis on sample tweets:")
        for i, tweet in enumerate(data[:3]):
            analysis = TextBlob(tweet['text'])
            polarity = analysis.sentiment.polarity
            predicted = 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'
            print(f"    Tweet {i+1}: '{tweet['text'][:50]}...'")
            print(f"      Actual: {tweet['sentiment']}, Predicted: {predicted}, Polarity: {polarity:.3f}")
    else:
        print(f"✗ {json_path} not found")

def test_sentiment_analyzer():
    """Test the SentimentAnalyzer class"""
    print("\n=== Testing SentimentAnalyzer Class ===")
    
    try:
        from scr.sentiment import SentimentAnalyzer
        
        csv_path = "data/raw_tweets.csv"
        if os.path.exists(csv_path):
            print(f"✓ Testing SentimentAnalyzer with {csv_path}")
            analyzer = SentimentAnalyzer(csv_path)
            
            # Test individual sentiment analysis
            test_texts = [
                "I love this app!",
                "This is terrible.",
                "It's okay, nothing special."
            ]
            
            print("  - Testing individual sentiment analysis:")
            for text in test_texts:
                sentiment = analyzer.analyze_sentiment(text)
                print(f"    '{text}' -> {sentiment}")
            
            # Test batch processing
            print("  - Testing batch processing...")
            analyzer.add_sentiment_column()
            
            # Save results
            output_path = "data/test_output.csv"
            analyzer.save_results(output_path)
            print(f"  - Saved results to {output_path}")
            
            # Verify output
            test_df = pd.read_csv(output_path)
            print(f"  - Output file contains {len(test_df)} rows")
            print(f"  - Output columns: {list(test_df.columns)}")
            
            # Clean up
            if os.path.exists(output_path):
                os.remove(output_path)
                print("  - Cleaned up test output file")
        else:
            print(f"✗ {csv_path} not found for SentimentAnalyzer test")
    except ImportError as e:
        print(f"✗ Could not import SentimentAnalyzer: {e}")
    except Exception as e:
        print(f"✗ Error testing SentimentAnalyzer: {e}")

def test_data_consistency():
    """Test data consistency between CSV and JSON"""
    print("\n=== Testing Data Consistency ===")
    
    csv_path = "data/raw_tweets.csv"
    json_path = "scr/raw_tweets .json"
    
    if os.path.exists(csv_path) and os.path.exists(json_path):
        print("✓ Both CSV and JSON files found")
        
        # Load CSV data
        df_csv = pd.read_csv(csv_path)
        
        # Load JSON data
        with open(json_path, 'r') as f:
            data_json = json.load(f)
        
        print(f"  - CSV has {len(df_csv)} tweets")
        print(f"  - JSON has {len(data_json)} tweets")
        
        # Compare structure
        csv_columns = set(df_csv.columns)
        json_keys = set(data_json[0].keys()) if data_json else set()
        
        print(f"  - CSV columns: {csv_columns}")
        print(f"  - JSON keys: {json_keys}")
        
        if csv_columns == json_keys:
            print("  ✓ CSV and JSON have consistent structure")
        else:
            print("  ✗ CSV and JSON have different structure")
        
        # Compare sample data
        if len(df_csv) > 0 and len(data_json) > 0:
            csv_sample = df_csv.iloc[0]
            json_sample = data_json[0]
            
            print("  - Comparing first tweet:")
            print(f"    CSV: {dict(csv_sample)}")
            print(f"    JSON: {json_sample}")
            
            # Check if they're the same
            csv_dict = csv_sample.to_dict()
            if all(str(csv_dict.get(k, '')) == str(json_sample.get(k, '')) for k in json_sample.keys()):
                print("  ✓ First tweets match")
            else:
                print("  ✗ First tweets don't match")
    else:
        print("✗ Cannot compare: missing CSV or JSON file")

def main():
    """Run all tests"""
    print("Twitter Sentiment Analysis - Data Testing")
    print("=" * 50)
    
    test_csv_data()
    test_json_data()
    test_sentiment_analyzer()
    test_data_consistency()
    
    print("\n" + "=" * 50)
    print("Testing completed!")

if __name__ == "__main__":
    main() 