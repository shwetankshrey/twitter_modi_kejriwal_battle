# Queries the all_tweets collection and creates a new collection with the distribution of categories.
import pymongo

client = pymongo.MongoClient()
db = client.kejri_modi
coll = db.all_tweets
toAdd = db.category_count

category_count = {"OT": 0, "RT":0}
for tweet in coll.find():
    md = tweet["Retweet"]
    if md:
        category_count["RT"] += 1 # Original Tweets
    else:
        category_count["OT"] += 1 # Re Tweets

jsonx = {"category": "OT", "hits": str(category_count["OT"])}
toAdd.insert_one(jsonx)
jsonx = {"category": "RT", "hits": str(category_count["RT"])}
toAdd.insert_one(jsonx)