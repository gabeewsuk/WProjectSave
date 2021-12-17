from db.Helpers.dbConnect import connect
from datetime import datetime as d


#Finding user and updating with correct trimmed schema
def findAndUpdatePost(db, user):
    date = d.now()
    #print(user)
    print(str(user)+"\n\n\n")
    

    #check if user exitss
        #updating db if it does not exist
    #try:
    
    print(len(user))
    db.Hashtags.find_one_and_update({"linkToPost":user[5]},
    {"$set":
    {"followers":user[1],
    'username': user[0],
    "profilepic_url":user[2],
    "postComments":user[3],
    "postLikes":user[4],
    "Description":user[6],
    "lastUserUpdate":date.strftime("%Y-%m-%d %H:%M:%S")}},upsert = True)
    #except Exception as Exc:
        #print("!!!!!!!findAndUpdate.py!!!!!")
        #print(Exc)
    return
