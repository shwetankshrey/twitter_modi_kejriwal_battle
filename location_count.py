# Queries the all_tweets collection and creates a new collection with the distribution of locations.
import json, urllib, pymongo, requests
KEY = "AIzaSyDPhMMoBq_AN7oqOp4xjpSQW2z9SI0i8bY" # Google Places API Key

client = pymongo.MongoClient()
db = client.kejri_modi
coll = db.all_tweets
toAdd = db.location_count

def get_location(search_text): # Puts a REST request to Google Places API and extracts the city.
    try:
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
        key = '?key=' + KEY
        query = '&query=' + urllib.parse.quote(search_text)
        url = url + key + query
        response = json.loads(requests.get(url).text)
        addr = response["results"][0]["formatted_address"]
        city = addr.split(", ")[0]
        country = addr.split(", ")[2]
        if country != "India":
            raise IndexError
    except IndexError:
        city = "India"
    return city # If city cannot be found / city not given (most common case), city set to India

i = 0
location_count = {}
for tweet in coll.find():
    i += 1
    loc = get_location(tweet["location"]) # Creation of collection.
    if loc not in location_count:
        location_count[loc] = 1
    else:
        location_count[loc] += 1
    if i%10 == 0:
        print(str(i) + " of 10000 done") # Takes time. Need to keep track of progress.

for x in location_count:
    jsonx = {"city": x, "tweets": str(location_count[x])}
    toAdd.insert_one(jsonx) # Document made