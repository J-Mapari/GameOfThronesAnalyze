import os
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

dialogue_counts = {}

directory = 'Name'
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        
        character_name = filename.split('.')[0]
        
        dialogue_counts[character_name] = len(df)

conn = sqlite3.connect('got_dialogues.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS dialogue_counts (
        character_name TEXT PRIMARY KEY,
        dialogue_count INTEGER
    )
''')

for character, count in dialogue_counts.items():
    cursor.execute('''
        INSERT INTO dialogue_counts (character_name, dialogue_count)
        VALUES (?, ?)
        ON CONFLICT(character_name) DO UPDATE SET dialogue_count = excluded.dialogue_count
    ''', (character, count))

conn.commit()
conn.close()

conn = sqlite3.connect('got_dialogues.db')
query = '''
    SELECT character_name, dialogue_count
    FROM dialogue_counts
    ORDER BY dialogue_count DESC
    LIMIT 20
'''
top_14_characters_df = pd.read_sql(query, conn)
conn.close()

plt.figure(figsize=(12, 8))
plt.barh(top_14_characters_df['character_name'], top_14_characters_df['dialogue_count'], color='skyblue')
plt.xlabel('Number of Dialogues')
plt.ylabel('Character Name')
plt.title('Top 20 Talkative Characters in Game of Thrones')
plt.gca().invert_yaxis() 

os.makedirs('basic_analysis', exist_ok=True)
plt.savefig('basic_analysis/top_14_names.png')

## Show the bar chart
#plt.show()
