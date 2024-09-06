import os
import re
import pandas as pd
from textblob import TextBlob
from collections import Counter
import matplotlib.pyplot as plt
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

def clean_text(text, stoplist):
    words = re.findall(r'\w+', text.lower()) 
    filtered_words = [word for word in words if word not in stoplist]
    return ' '.join(filtered_words)

def sentiment_analysis(text):
    scores = sid.polarity_scores(text)
    return scores['pos'], scores['neg'], scores['neu'], scores['compound']  

with open('stoplist.txt', 'r', encoding = "utf-8") as f:
    stoplist = set(f.read().splitlines())

character_sentiments = {}

directory = 'Name'
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        
        character_name = filename.split('.')[0]
        
        character_dialogue = ' '.join(df['Sentence'].astype(str))
        
        clean_dialogue = clean_text(character_dialogue, stoplist)
        
        pos, neg, neu, compound = sentiment_analysis(clean_dialogue)
        
        character_sentiments[character_name] = {
            'Positive': pos,
            'Negative': neg,
            'Neutral': neu,
            'Compound': compound
        }

sentiment_df = pd.DataFrame.from_dict(character_sentiments, orient='index')

plt.figure(figsize=(12, 8))

plt.bar(sentiment_df.index, sentiment_df['Positive'], color='green', alpha=0.6, label='Positive')

plt.bar(sentiment_df.index, sentiment_df['Negative'], color='red', alpha=0.6, bottom=sentiment_df['Positive'], label='Negative')

plt.bar(sentiment_df.index, sentiment_df['Neutral'], color='gray', alpha=0.6, bottom=sentiment_df['Positive'] + sentiment_df['Negative'], label='Neutral')

plt.xlabel('Character')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Analysis of Game of Thrones Characters')
plt.xticks(rotation=90)
plt.legend()

os.makedirs('sentiment_analysis', exist_ok=True)
plt.savefig('sentiment_analysis/character_sentiments.png')


sentiment_df.to_csv('sentiment_analysis/character_sentiments.csv')
