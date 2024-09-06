# Game of Thrones Analysis

## Project Overview

This project has analysis of dialogues and character sentiments from the "Game of Thrones" series. The goal is to explore dialogue density, character sentiments, and visual representations of key characters' dialogues.

## Project Structure
├── .idea
│   ├── .gitignore
│   ├── GameOfThronesAnalyze.iml
│   ├── misc.xml
│   ├── modules.xml
│   ├── vcs.xml
│   └── workspace.xml
├── basic_analysis
│   ├── bar.png
│   ├── basic_analysis.py
│   ├── dialogue_density.png
│   └── pie.png
├── character_specific
│   ├── character_sentiment.py
│   ├── character_word_frequency.py
│   └── character_word_frequency
│       ├── Alliser Thorne_wordcloud.png
│       ├── Arya Stark_wordcloud.png
│       ├── Barristan Selmy_wordcloud.png
│       ├── Benjen Stark_wordcloud.png
│       ├── Beric Dondarrion_wordcloud.png
│       ├── Bran Stark_wordcloud.png
│       ├── Bronn_wordcloud.png
│       ├── Catelyn Stark_wordcloud.png
│       ├── Cersei Lannister_wordcloud.png
│       ├── Craster_wordcloud.png
│       ├── Daario Naharis_wordcloud.png
│       ├── Daenerys Targaryen_wordcloud.png
│       ├── Eddard Stark_wordcloud.png
│       ├── Euron Greyjoy_wordcloud.png
│       ├── Gilly_wordcloud.png
│       ├── Grey Worm_wordcloud.png
│       ├── Hodor_wordcloud.png
│       ├── Hot Pie_wordcloud.png
│       ├── Jaime Lannister_wordcloud.png
│       ├── Janos Slynt_wordcloud.png
│       ├── Jeor Mormont_wordcloud.png
│       ├── Jon Snow_wordcloud.png
│       ├── Jorah Mormont_wordcloud.png
│       ├── Khal Drogo_wordcloud.png
│       ├── Kraznys mo Nakloz_wordcloud.png
│       ├── Lady Crane_wordcloud.png
│       ├── Lancel Lannister_wordcloud.png
│       ├── Leaf_wordcloud.png
│       ├── Loras Tyrell_wordcloud.png
│       ├── Lysa Arryn_wordcloud.png
│       ├── Mace Tyrell_wordcloud.png
│       ├── Maester Aemon_wordcloud.png
│       ├── Maester Pycelle_wordcloud.png
│       ├── Margaery Tyrell_wordcloud.png
│       ├── Melisandre_wordcloud.png
│       ├── Meryn Trant_wordcloud.png
│       ├── Mirri Maz Duur_wordcloud.png
│       ├── Missandei_wordcloud.png
│       ├── Oberyn Martell_wordcloud.png
│       ├── Olenna Tyrell_wordcloud.png
│       ├── Olly_wordcloud.png
│       ├── Osha_wordcloud.png
│       ├── Pyat Pree_wordcloud.png
│       ├── Qyburn_wordcloud.png
│       ├── Ramsay Bolton_wordcloud.png
│       ├── Renly Baratheon_wordcloud.png
│       ├── Rickard Karstark_wordcloud.png
│       ├── Rickon Stark_wordcloud.png
│       ├── Robb Stark_wordcloud.png
│       ├── Robert Baratheon_wordcloud.png
│       ├── Robin Arryn_wordcloud.png
│       ├── Roose Bolton_wordcloud.png
│       ├── Ros_wordcloud.png
│       ├── Sansa Stark_wordcloud.png
│       ├── Shae_wordcloud.png
│       ├── Stannis Baratheon_wordcloud.png
│       ├── Syrio Forel_wordcloud.png
│       ├── Theon Greyjoy_wordcloud.png
│       ├── Tyrion Lannister_wordcloud.png
│       ├── Tywin Lannister_wordcloud.png
│       ├── Varys_wordcloud.png
│       ├── Walder Frey_wordcloud.png
│       ├── Will_wordcloud.png
│       ├── Wun Wun_wordcloud.png
│       ├── Yara Greyjoy_wordcloud.png
│       └── Ygritte_wordcloud.png
├── Episode
│   ├── Episode 1.csv
│   ├── Episode 10.csv
│   ├── Episode 2.csv
│   ├── Episode 3.csv
│   ├── Episode 4.csv
│   ├── Episode 5.csv
│   ├── Episode 6.csv
│   ├── Episode 7.csv
│   ├── Episode 8.csv
│   └── Episode 9.csv
├── Name
│   ├── Alliser Thorne.csv
│   ├── Arya Stark.csv
│   ├── Barristan Selmy.csv
│   ├── Benjen Stark.csv
│   ├── Beric Dondarrion.csv
│   ├── Bran Stark.csv
│   ├── Bronn.csv
│   ├── Catelyn Stark.csv
│   ├── Cersei Lannister.csv
│   ├── Craster.csv
│   ├── Daario Naharis.csv
│   ├── Daenerys Targaryen.csv
│   ├── Eddard Stark.csv
│   ├── Euron Greyjoy.csv
│   ├── Gilly.csv
│   ├── Grey Worm.csv
│   ├── Hodor.csv
│   ├── Hot Pie.csv
│   ├── Jaime Lannister.csv
│   ├── Janos Slynt.csv
│   ├── Jeor Mormont.csv
│   ├── Jon Snow.csv
│   ├── Jorah Mormont.csv
│   ├── Khal Drogo.csv
│   ├── Kraznys mo Nakloz.csv
│   ├── Lady Crane.csv
│   ├── Lancel Lannister.csv
│   ├── Leaf.csv
│   ├── Loras Tyrell.csv
│   ├── Lysa Arryn.csv
│   ├── Mace Tyrell.csv
│   ├── Maester Aemon.csv
│   ├── Maester Pycelle.csv
│   ├── Margaery Tyrell.csv
│   ├── Melisandre.csv
│   ├── Meryn Trant.csv
│   ├── Mirri Maz Duur.csv
│   ├── Missandei.csv
│   ├── Oberyn Martell.csv
│   ├── Olenna Tyrell.csv
│   ├── Olly.csv
│   ├── Osha.csv
│   ├── Pyat Pree.csv
│   ├── Qyburn.csv
│   ├── Ramsay Bolton.csv
│   ├── Renly Baratheon.csv
│   ├── Rickard Karstark.csv
│   ├── Rickon Stark.csv
│   ├── Robb Stark.csv
│   ├── Robert Baratheon.csv
│   ├── Robin Arryn.csv
│   ├── Roose Bolton.csv
│   ├── Ros.csv
│   ├── Sansa Stark.csv
│   ├── Shae.csv
│   ├── Stannis Baratheon.csv
│   ├── Syrio Forel.csv
│   ├── Theon Greyjoy.csv
│   ├── Tyrion Lannister.csv
│   ├── Tywin Lannister.csv
│   ├── Varys.csv
│   ├── Walder Frey.csv
│   ├── Will.csv
│   ├── Wun Wun.csv
│   ├── Yara Greyjoy.csv
│   └── Ygritte.csv
├── Seasons
│   ├── Season 1.csv
│   ├── Season 2.csv
│   ├── Season 3.csv
│   ├── Season 4.csv
│   ├── Season 5.csv
│   ├── Season 6.csv
│   ├── Season 7.csv
│   └── Season 8.csv
├── sentiment_analysis
│   ├── character_sentiments.csv
│   └── character_sentiments.png
├── directory_structure.txt
├── game_of_thrones_data.csv
├── got_dialogues.db
├── got_word_counts.db
├── LICENSE
└── README.md



