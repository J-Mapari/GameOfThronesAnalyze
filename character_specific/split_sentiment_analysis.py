import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

def clean_text(text, stoplist):
    words = re.findall(r'\w+', text.lower())
    filtered_words = [word for word in words if word not in stoplist]
    return ' '.join(filtered_words)
def sentiment_analysis(text):
    scores = sid.polarity_scores(text)
    return scores['pos'], scores['neg'], scores['neu'], scores['compound']
with open('stoplist.txt', 'r', encoding="utf-8") as f:
    stoplist = set(f.read().splitlines())

data_file = 'game_of_thrones_data.csv'
df = pd.read_csv(data_file)

def process_dialogues(df):
    grouped = df.groupby(['Season', 'Episode'])

    for (season, episode), group in grouped:
        character_sentiments = {}
        
        for _, row in group.iterrows():
            character_name = row['Name']
            character_dialogue = str(row['Sentence'])
            
            clean_dialogue = clean_text(character_dialogue, stoplist)
            pos, neg, neu, compound = sentiment_analysis(clean_dialogue)
            
            if character_name in character_sentiments:
                character_sentiments[character_name]['Positive'] += pos
                character_sentiments[character_name]['Negative'] += neg
                character_sentiments[character_name]['Neutral'] += neu
                character_sentiments[character_name]['Compound'] += compound
            else:
                character_sentiments[character_name] = {
                    'Positive': pos,
                    'Negative': neg,
                    'Neutral': neu,
                    'Compound': compound
                }

        sentiment_df = pd.DataFrame.from_dict(character_sentiments, orient='index')
        sentiment_df.index = sentiment_df.index.astype(str)
        plt.figure(figsize=(14, 8))
        plt.bar(sentiment_df.index, sentiment_df['Positive'], color='green', alpha=0.6, label='Positive')
        plt.bar(sentiment_df.index, sentiment_df['Negative'], color='red', alpha=0.6, bottom=sentiment_df['Positive'], label='Negative')
        plt.bar(sentiment_df.index, sentiment_df['Neutral'], color='gray', alpha=0.6, bottom=sentiment_df['Positive'] + sentiment_df['Negative'], label='Neutral')
        plt.xlabel('Character')
        plt.ylabel('Sentiment Score')
        plt.title(f'Sentiment Analysis of Game of Thrones Characters - Season {season}, Episode {episode}')
        plt.xticks(rotation=45, ha='right', fontsize=8)
        plt.margins(0)
        plt.legend()
        output_dir = f'sentiment_analysis/Season_{season}/Episode_{episode}'
        os.makedirs(output_dir, exist_ok=True)
        plot_path = os.path.join(output_dir, 'character_sentiments.png')
        plt.savefig(plot_path)
        csv_path = os.path.join(output_dir, 'character_sentiments.csv')
        sentiment_df.to_csv(csv_path)

        plt.close()  

process_dialogues(df)
