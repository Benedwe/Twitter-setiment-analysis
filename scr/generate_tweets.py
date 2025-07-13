import pandas as pd
import random
from datetime import datetime, timedelta
import json

class TweetGenerator:
    def __init__(self):
        self.positive_templates = [
            "I love {topic}! {positive_phrase}",
            "Amazing {topic}! {positive_phrase}",
            "So happy with {topic}! {positive_phrase}",
            "Best {topic} ever! {positive_phrase}",
            "Incredible {topic}! {positive_phrase}",
            "Fantastic {topic}! {positive_phrase}",
            "Wonderful {topic}! {positive_phrase}",
            "Excellent {topic}! {positive_phrase}",
            "Brilliant {topic}! {positive_phrase}",
            "Outstanding {topic}! {positive_phrase}"
        ]
        
        self.negative_templates = [
            "I hate {topic}! {negative_phrase}",
            "Terrible {topic}! {negative_phrase}",
            "Awful {topic}! {negative_phrase}",
            "Worst {topic} ever! {negative_phrase}",
            "Disappointing {topic}! {negative_phrase}",
            "Frustrating {topic}! {negative_phrase}",
            "Annoying {topic}! {negative_phrase}",
            "Useless {topic}! {negative_phrase}",
            "Broken {topic}! {negative_phrase}",
            "Ridiculous {topic}! {negative_phrase}"
        ]
        
        self.neutral_templates = [
            "I think {topic} is {neutral_phrase}",
            "Not sure about {topic}. {neutral_phrase}",
            "Mixed feelings about {topic}. {neutral_phrase}",
            "I guess {topic} is {neutral_phrase}",
            "Maybe {topic} is {neutral_phrase}",
            "I suppose {topic} is {neutral_phrase}",
            "Not bad, not great - {topic} is {neutral_phrase}",
            "I'm indifferent to {topic}. {neutral_phrase}",
            "It's okay, {topic} is {neutral_phrase}",
            "I don't have strong feelings about {topic}. {neutral_phrase}"
        ]
        
        self.topics = [
            "Twitter", "social media", "the new update", "the app", "the interface",
            "the features", "the design", "the platform", "the community", "the algorithm",
            "the notifications", "the search", "the timeline", "the trending topics",
            "the dark mode", "the mobile app", "the web version", "the API", "the security",
            "the privacy settings", "the verification", "the blue checkmark", "the hashtags",
            "the retweets", "the likes", "the replies", "the DMs", "the spaces", "the lists"
        ]
        
        self.positive_phrases = [
            "it's absolutely fantastic!", "can't get enough of it!", "it's changed my life!",
            "it's exactly what I needed!", "it's so intuitive!", "it's incredibly useful!",
            "it's made everything better!", "it's so well designed!", "it's revolutionary!",
            "it's the best thing ever!", "it's so user-friendly!", "it's incredibly fast!",
            "it's so reliable!", "it's exceeded my expectations!", "it's pure genius!"
        ]
        
        self.negative_phrases = [
            "it's completely broken!", "it's driving me crazy!", "it's so frustrating!",
            "it's a complete disaster!", "it's unusable!", "it's so slow!",
            "it's constantly crashing!", "it's so confusing!", "it's a waste of time!",
            "it's the worst decision ever!", "it's so buggy!", "it's completely useless!",
            "it's making me angry!", "it's so unreliable!", "it's a total mess!"
        ]
        
        self.neutral_phrases = [
            "alright I suppose", "not too bad", "could be worse", "it's fine",
            "does the job", "gets the work done", "not amazing but not terrible",
            "average at best", "mediocre", "passable", "acceptable", "tolerable",
            "not great but not awful", "it is what it is", "meh"
        ]
        
        self.usernames = [
            "alice", "bob", "charlie", "dana", "ed", "frank", "grace", "harry", "ivy", "jack",
            "kate", "liam", "mona", "nick", "olivia", "paul", "quinn", "rose", "sam", "tina",
            "uma", "victor", "will", "xena", "yara", "zane", "amy", "ben", "claire", "dan",
            "ella", "fred", "gina", "henry", "iris", "june", "karl", "lisa", "matt", "nina",
            "otto", "pam", "quincy", "rachel", "steve", "tara", "ursula", "vin", "wanda", "xavier",
            "yuki", "zara", "alex", "blake", "casey", "drew", "emery", "finley", "gray", "hunter",
            "indigo", "jordan", "kendall", "logan", "morgan", "noah", "oliver", "parker", "quinn", "riley",
            "sage", "taylor", "unisex", "val", "winter", "xander", "yves", "zen"
        ]

    def generate_tweet(self, sentiment=None):
        if sentiment is None:
            sentiment = random.choice(['positive', 'negative', 'neutral'])
        
        topic = random.choice(self.topics)
        
        if sentiment == 'positive':
            template = random.choice(self.positive_templates)
            phrase = random.choice(self.positive_phrases)
        elif sentiment == 'negative':
            template = random.choice(self.negative_templates)
            phrase = random.choice(self.negative_phrases)
        else:
            template = random.choice(self.neutral_templates)
            phrase = random.choice(self.neutral_phrases)
        
        text = template.format(topic=topic, positive_phrase=phrase, negative_phrase=phrase, neutral_phrase=phrase)
        
        # Add some hashtags occasionally
        if random.random() < 0.3:
            hashtags = ["#Twitter", "#SocialMedia", "#Tech", "#Update", "#App"]
            text += f" {random.choice(hashtags)}"
        
        # Add mentions occasionally
        if random.random() < 0.2:
            mention = random.choice(self.usernames)
            text += f" @{mention}"
        
        return {
            'text': text,
            'sentiment': sentiment,
            'username': random.choice(self.usernames)
        }

    def generate_dataset(self, num_tweets=200):
        tweets = []
        
        # Generate a balanced dataset
        positive_count = num_tweets // 3
        negative_count = num_tweets // 3
        neutral_count = num_tweets - positive_count - negative_count
        
        # Generate positive tweets
        for i in range(positive_count):
            tweet = self.generate_tweet('positive')
            tweet['tweet_id'] = len(tweets) + 1
            tweets.append(tweet)
        
        # Generate negative tweets
        for i in range(negative_count):
            tweet = self.generate_tweet('negative')
            tweet['tweet_id'] = len(tweets) + 1
            tweets.append(tweet)
        
        # Generate neutral tweets
        for i in range(neutral_count):
            tweet = self.generate_tweet('neutral')
            tweet['tweet_id'] = len(tweets) + 1
            tweets.append(tweet)
        
        # Shuffle the dataset
        random.shuffle(tweets)
        
        return tweets

    def save_to_csv(self, tweets, filename="data/raw_tweets.csv"):
        df = pd.DataFrame(tweets)
        df.to_csv(filename, index=False)
        print(f"Generated {len(tweets)} tweets and saved to {filename}")
        return df

    def save_to_json(self, tweets, filename="scr/raw_tweets.json"):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(tweets, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(tweets)} tweets to {filename}")

if __name__ == "__main__":
    generator = TweetGenerator()
    
    # Generate 200 tweets
    tweets = generator.generate_dataset(200)
    
    # Save to both CSV and JSON formats
    generator.save_to_csv(tweets)
    generator.save_to_json(tweets)
    
    # Print some statistics
    sentiment_counts = {}
    for tweet in tweets:
        sentiment = tweet['sentiment']
        sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
    
    print("\nDataset Statistics:")
    for sentiment, count in sentiment_counts.items():
        print(f"{sentiment.capitalize()}: {count} tweets ({count/len(tweets)*100:.1f}%)")
    
    print(f"\nTotal tweets generated: {len(tweets)}") 