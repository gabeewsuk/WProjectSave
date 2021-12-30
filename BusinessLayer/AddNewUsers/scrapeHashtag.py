from pymongo import MongoClient
import time
import concurrent.futures
import requests
from datetime import datetime as d
import sys, os
sys.path.append(os.path.abspath(os.path.join('../../..', 'WellsSoftware')))

from db.Helpers.dbConnect import connect

from routes.getHashtag.getHashtagData import getHashTagStats
from routes.getUserPost.getUserPostData import getPostStats
from db.findNUpdate.findAndUpdate import findAndUpdatePost



#updates sent in users with user posts
def newHashTag(hashtags):
    
    db = connect('WellsData')
    shortcodes = getHashTagStats(hashtags)
    temp = []
    temp2 = 0
    print(len(shortcodes))
    shortcodes2 =[]
    print(shortcodes)
    #time.sleep()

    for x in shortcodes:
        for y in x:
            #print(y)
        
            temp2+=1
            #must be 1 less than what is shown ie. 659 is 658
            if temp2 >= 8207:
                temp.append(y)
            print(temp2)
        
    print("yo")
    shortcodes2.append(temp)
    print(len(temp))
    print(len(shortcodes2))
    print(len(shortcodes))
    #time.sleep(20)
    subset = []
    i = 0
    for hashtag in shortcodes2:
        #print(x)
        userCount = len(hashtag)
        for post in hashtag:
            
            subset.append(post)
            #print(subset)
            if i % 200 == 0 or (userCount < 200 and i % 50 == 0) or (userCount < 50 and i % 10 == 0) or userCount<10:
                users = getPostStats(subset)
                with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
                    future_to_url = (executor.submit(findAndUpdatePost, db,  user)for user in users)
                    time1 = time.time()
                    for future in concurrent.futures.as_completed(future_to_url):
                        try:
                            data = future.result()
                        except Exception as exc:
                            print(exc)
                        finally:
                            NAN = 0

                    time2 = time.time()
                print(f'Took {time2-time1:.2f} s')
                subset = []
            i+=1
            userCount-=1

        print("Done updating userPosts!")

#newHashTag(["saberslice","gabearmy", "bbowlflyin"])



