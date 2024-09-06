import os
import re
import pandas as pd
from collections import Counter
import sqlite3
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def word_count(text, stoplist):
    words = re.findall(r'\w+', text.lower())
    filtered_words = [word for word in words if word not in stoplist]
    return Counter(filtered_words)

with open('stoplist.txt', 'r', encoding='utf-8') as f:
    stoplist = set(f.read().splitlines())

character_sentences = {}

directory = 'Name'
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        
        character_name = filename.split('.')[0]
        
        character_sentences[character_name] = ' '.join(df['Sentence'].astype(str))

conn = sqlite3.connect('got_word_counts.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS word_counts (
        character_name TEXT,
        word TEXT,
        count INTEGER,
        PRIMARY KEY (character_name, word)
    )
''')

for character_name, sentences in character_sentences.items():
    word_freqs = word_count(sentences, stoplist)
    
    for word, count in word_freqs.items():
        cursor.execute('''
            INSERT INTO word_counts (character_name, word, count)
            VALUES (?, ?, ?)
            ON CONFLICT(character_name, word) DO UPDATE SET count = excluded.count
        ''', (character_name, word, count))

conn.commit()
conn.close()

output_directory = 'character_word_frequency'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

conn = sqlite3.connect('got_word_counts.db')
cursor = conn.cursor()

cursor.execute('SELECT DISTINCT character_name FROM word_counts')
characters = cursor.fetchall()

for character in characters:
    character_name = character[0]

    query = '''
        SELECT word, count
        FROM word_counts
        WHERE character_name = ?
        ORDER BY count DESC
    '''
    cursor.execute(query, (character_name,))
    word_counts = dict(cursor.fetchall())

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    file_path = os.path.join(output_directory, f'{character_name}_wordcloud.png')
    plt.savefig(file_path)
    plt.close()

conn.close()
