#!/bin/sh
terminal -e mongod # First started the Mongo DB server
python get_tweets.py # Next extracted 10k tweets and added to a common collection.
python category_count.py # Distributed to categories
python fav_count.py # Classified according to facorites count on original tweets.
python hash_count.py # Sorted and found the 10 most common hashtags.
python location_count.py # Checked where the tweet was from. // Need to work upon this.
python type_count.py # Distributed according to types of content.
# Dumping all the collections made into JSON files.
mongoexport --db kejri_modi --collection all_tweets --out dumped_dbs/all_tweets.json
mongoexport --db kejri_modi --collection category_count --out dumped_dbs/category_count.json
mongoexport --db kejri_modi --collection hash_count --out dumped_dbs/hash_count.json
mongoexport --db kejri_modi --collection fav_count --out dumped_dbs/fav_count.json
mongoexport --db kejri_modi --collection location_count --out dumped_dbs/location_count.json
mongoexport --db kejri_modi --collection type_count --out dumped_dbs/type_count.json
# Starting the Flask server.
python main.py
# Opening the web app on Chrome.
google-chrome http://localhost:5000