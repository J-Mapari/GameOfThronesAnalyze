# GameOfThronesAnalyze

## Introduction
This data analysis project explores **Game of Thrones**, one of my favorite shows, by examining dialogue sentiment, basic dialogue quantity, and dialogue density.

## Table of Contents
- [Method](#method)
- [Conclusion](#conclusion)
  - [Basic Analysis](#basic-analysis)
  - [Character-wise Analysis](#character-wise-analysis)
  - [Sentiment Analysis](#sentiment-analysis)
  - [Seasonal Sentiment Analysis](#seasonal-sentiment-analysis)
  - [Dialogue Density](#dialogue-density)
- [Credits](#credits)

## Method
- **Software Used:** Visual Studio Code, Windows
- **Languages:** Jupyter Notebooks, Python
- **Libraries:** Pandas, os, math, nltk, matplotlib

## Conclusion

### Basic Analysis

#### Character Analysis
The 20 most talkative characters (measured by the number of dialogues) are illustrated below:
![Top 20 Most Talkative Characters](https://github.com/J-Mapari/GameOfThronesAnalyze/blob/main/basic_analysis/bar.png)

This visualization highlights that the Lannisters have the highest number of dialogues. Tyrion Lannister leads the way, followed by Jon Snow and Daenerys Targaryen. This graph provides insight into the characters who dominate the show in terms of dialogue volume.

The top 15 most influential characters, measured by the percentage of overall dialogues, are shown below:
![Top 15 Influential Characters](https://github.com/J-Mapari/GameOfThronesAnalyze/blob/main/basic_analysis/pie.png)

Tyrion Lannister contributes 17.7% of the dialogues among the top 25 characters. This analysis shows the significant presence of key characters like Tywin Lannister and Eddard Stark, with the Starks and Lannisters dominating the show.

### Character-wise Analysis

Word clouds for the top 50 characters have been created to analyze frequently used words. Common words are filtered out using a stoplist. Key observations include:
- **Stark Family:** Arya and Bran have unique word clouds with words like "Kill" and "Hodor", respectively.
- **Jon Snow:** His focus on the wall is evident with frequent mentions of "wall", "night", and "king".
- **Daenerys Targaryen:** Her word cloud reflects her dedication to the "people" and dragons.
- **Hodor:** True to his nature, "Hodor" is the most frequently used word.

Example word cloud for Melisandre:
![Melisandre's Word Cloud](https://github.com/J-Mapari/GameOfThronesAnalyze/blob/main/character_specific/character_word_frequency/Melisandre_wordcloud.png)

### Sentiment Analysis

Sentiment analysis reveals the general tone of characters throughout the series:
- **Villains:** Ramsay Bolton and Cersei Lannister have high negative sentiment scores, reflecting their cruel nature.
- **Stark Family:** Their dialogues show a generally negative sentiment, indicating their ongoing hardships.
- **Melisandre:** Her references to killings and sacrifices contribute to a high negative score.
- **Arya Stark:** Displays high negativity, reflecting her journey and anger.
- **Hodor:** Maintains a neutral sentiment.

Complete sentiment analysis graph:
![Character Sentiment Analysis](https://github.com/J-Mapari/GameOfThronesAnalyze/blob/main/sentiment_analysis/character_sentiments.png)

### Seasonal Sentiment Analysis

Sentiment analysis was conducted for every episode across all seasons, revealing the mood of characters at various phases of the series:
- **Tyrion Lannister:** His positivity increases as victory approaches but shifts to negativity after a moral loss.
- **Sandor Clegane:** His negativity rises as his storyline nears its end.
- **Daenerys Targaryen:** Displays more positive sentiment as she prepares for major battles, reflecting her confidence.

Example from Season 7, Episode 1:
![Season 7, Episode 1 Sentiment Analysis](https://github.com/J-Mapari/GameOfThronesAnalyze/blob/main/sentiment_analysis/Season_Season%207/Episode_Episode%201/character_sentiments.png)

### Dialogue Density

Dialogue density was calculated per season and episode, illustrating the sheer volume of fight scenes in later seasons with noticeable drops.

![Dialogue Density](https://github.com/J-Mapari/GameOfThronesAnalyze/blob/main/basic_analysis/dialogue_density.png)

## Credits
- [Stoplist](https://github.com/stopwords-iso/stopwords-en/blob/master/stopwords-en.txt)
- [Dataset](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons)
