# Backend to act as the interface between the front end and the MongoDB collections.
from flask import Flask, render_template
import pymongo

client = pymongo.MongoClient()
db = client.kejri_modi
lc = db.location_count
hc = db.hash_count
tc = db.type_count
cc = db.category_count
fc = db.fav_count
# Calling all collections
app = Flask(__name__)
# 3. 2. 1..
@app.route('/') # STAAART!!
def main():
    loc = []
    cat = []
    typ = []
    has = []
    fav = [] # Created dicts to be sent to the template.
    for a in lc.find():
        loc.append({"city":a["city"], "tweets":a["tweets"]}) # Initialising those templates.
    for a in cc.find():
        cat.append(a["hits"]) # Initialising those templates.
    for a in tc.find():
        typ.append(a["hits"]) # Initialising those templates.
    i = 1
    for a in hc.find():
        has.append({"index":i, "hashtag":a["hashtag"], "count":a["count"]}) # Initialising those templates.
        i+=1
    for a in fc.find():
        fav.append({"favs":str(a["favs"]), "count":a["count"]})# Initialising those templates.
    return render_template('index.html', location_count=loc, category_count=cat, type_count=typ, hash_count=has, fav_count=fav) # Send the dicts to template.

    # FINISH LINE


if __name__ == '__main__':
    app.run(debug=True)
