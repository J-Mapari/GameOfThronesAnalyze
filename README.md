# GameOfThronesAnalyze
## Introduction
Data analysis project, to analyse Game of Thrones, one of my most beloved shows, by dialogues sentiment, basic dialogue quantity and dialogue density. 

## Table of Contents
- [Method](#Method)
- [Conclusion](#Conclusion)
- [Credits](#Credit)

## Method
- Software used: Visual Studio Code, Windows.
- Languages: Jupyter Notebooks, Python.
- Libraries (not all): Pandas, os, math, nltk, matplotlib

## Conclusion
### Basic analysis
#### Character analysis
The 20 most talkative characters (measured by number of dialogues) are given as follows:
![Book logo](/GameOfThronesAnalyze/bar.png)

We can see that Lannisters have the highest number of dialogues, Tyrion Lannister, who is one of the best characters in the show, leads the way, followed by Jon Snow and Dany. This is a simple visualisation to give an idea of who largely dominates the show.


The top 15 most influential characters in the show (measured as a percentage of the overall number of dialogues said by these characters): 
![logo](/GameOfThronesAnalyze/pie.png)

Of the total number of dialogues spoken by the top 25 characters, Tyrion has 17.7% of them, while there are not many interesting takeaways here, but we can observe that very important characters like Tywin Lannister
have similar proportions of the dialogues, to characters like Eddard Stark, who have a much shorter screentime. Also that the Starks and Lannisters dominate the show, but that was already a known fact before this analysis. 

### Character-wise analysis
Wordclouds for top 50 or so characters have been made, to analyse what words were used by each one and how frequently. I used a stoplist, to make sure common words were not displayed in the wordclouds. The data is stored in a database for future use/referece and some interesting takeaways are: 
- In the Stark family, only Arya and Bran did not have words which adress someone else, like "King", "Lord" or "Father". Arya and Bran's most used words were, "Kill" and "Hodor" respectively.
- Jon Snow's obsession with the wall is depicted here by "wall" being one of his most used words, "night" and "king" are not far off either, showing us how obsessed he is with the white walkers.
- Dany's dedication to be the "people's ruler" and her obsession with dragons is visible in her wordcloud, "People" and "dragons" are two of her most used words.
- In classic Hodor fashion, the most used word by Hodor was indeed, "Hodor".
This is Melisandre's wordcloud:
![](/GameOfThronesAnalyze/Melisandre_wordcloud.png)

### Sentiment Analysis
I used sentiment analysis on characters to get their overall tone in the show, to understand what they sound like, what is their general outlook. Some interesting findings were: 
- Villians like Ramsay Bolton and Cersei had a very high negative score, suggesting the cruel nature of their dialogues.
- The Stark family's dialogue scores are also very negative, suggesting the hardship they faced throught the series.
- Melisandre is a very religious woman who made references to killings and sacrifices, which is displayed in her negativity score here.
- Arya stark has a very high negativity score, signifying her journey and the built up anger within her, references to murders and killings will likely have played a part in her score.
- Hodor is completely neutral.
Here is the entire graph:
![](/GameOfThronesAnalyze/character_sentiments.png)

### Seasonal Sentiment Analysis
There has been sentiment analysis for every episode in every season, it shows us the relative mood of characters at that phase of the series. 
- For example, the last few episodes have Tyrion Lannister's tone as victory is closer, while after his faction loses (morally) negativity is observed.
- Simiarly, Sandor's negativity increases when he does is close to his end and while fighting the white walkers.
- Dany's dialogues are more positive while going into the long night, and the last battle at King's landing, as she thinks she has a chance for victory, showing her confidence..
Example from S7E1:

![](/GameOfThronesAnalyze/sentiment_analysis/Season_Season 7/Episode_Episode 1/character_sentiments.png)



### Dialogue density
I calculated dialogue density, per season per episode and made a graph. It does signify the sheer number of fight scenes in the later seasons, with the sharp drop. 

![](/GameOfThronesAnalyze/basic_analysis/dialogue_density.png)

## Credits
- [stoplist](https://github.com/stopwords-iso/stopwords-en/blob/master/stopwords-en.txt)
- [dataset](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons)

