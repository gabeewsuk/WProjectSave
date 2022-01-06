from pymongo import MongoClient
import time
import concurrent.futures
import requests
from datetime import datetime as d
import sys, os
sys.path.append(os.path.abspath(os.path.join('../../..', 'WellsSoftware')))

from  BusinessLayer.AddNewUsers.new import scrapeTenLeads





#updates sent in users with user posts
def newHashTag(hashtags):
    scrapeTenLeads()
    
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        future_to_url = (executor.submit(scrapeTenLeads,  hashtag)for hashtag in hashtags)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
            except Exception as exc:
                print(exc)
            finally:
                NAN = 0

                    