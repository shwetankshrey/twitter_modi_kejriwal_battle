# Modi vs Kejriwal - The Battle of Tweets

Let's face it, it is 2017 and the entire world is on social media. You could predict what is going to happen in real life by analyzing the trends on social media. This web app that I have made has a similar use. It is supposed to analyze the social media presence and recognition as well as popularity of two rival leaders- Narendra Modi and Arvind Kejriwal.

To do this I have scraped tweets with hashtags relevant to both leaders and have tried to present them in a pictorial manner using graphs and charts. The technologies that I have used here are:
  - Python ( To do all the scripting )
  - Tweepy ( Python Library which is a wrapper upon the Twitter API )
  - MongoDB ( To store the data in form of JSON documents stored in collections )
  - Google Places API ( To identify the origin of tweets better )
  - HTML-CSS-JS ( To create the front end for the web app to visualise the data )
  - Flask ( Python library which provides a backend to the web app )

# STEPS:
### Getting Tweets:

1) Created an instance of the Twitter API and authenticated it in Python using Tweepy.
2)  Created an instance of the MongoDB Client (having the MongoDB server opened on a terminal).
3)  Created a couple of queries having size less than 140 characters.
4)  Started the outer loop to run until 10k tweets extracted.
5)  Searched for the queries and iterated through the results.
6)  Storing required fields of the documents in a collection.

### Querying through tweets:
1) And adding them to different collections in accordance with the requirements of the subtask.
2) Dumping all the collections into JSON files.

### Starting the backend server:
1) Calling all the different collections.
2) Creating dictionaries for each to be passed to the template for rendering.
3) Rendering the templates.

### Running the web app:
1) Starting the servers for MongoDB as well as Flask.
2) ```python main.py```

# OR
### Terminal 1
```sh
$ mongod
```
### Terminal 2
```sh
$ python get_tweets.py
$ python category_count.py
$ python fav_count.py
$ python hash_count.py
$ python location_count.py
$ python type_count.py
$ python main.py
```
### Terminal 3
```sh
$ google-chrome http://localhost:5000
```
