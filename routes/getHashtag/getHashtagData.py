from pymongo import MongoClient
#import sys, os
import time
import concurrent.futures
import requests
from decouple import config
from routes.getHashtag.getRecursiveHashtag import getHashTagWhileLoop

#from Folder.db.Finders.dbFindUserNames import findUserNames




#getUserId from an array of usernames
def getHashTagStats(hashtags):
    querystrings = []
    out = []
    counter = 0

     
            

    url = config("API_URL")+"/hash_tag_medias_v2"


    headers = {
        'x-rapidapi-key': config("API_KEY"),
        'x-rapidapi-host': config("API_HOST")
        }



    def load_url(hashtag):
        response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag})
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag})
        return response.json()

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        future_to_url = (executor.submit(load_url, tag)for tag in hashtags)
        time1 = time.time()
        time4 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                out.append(data)
            except Exception as exc:
                print(exc)
            finally:
                time2 = time.time()
                time4 = time.time()    
                print(len(out))
                #print(f' reqest Took {time2-time1:.2f} s')

                

        time2 = time.time()
    print(f'Took {time2-time1:.2f} s')
    print(len(out))
    #print(out)
    post_ids = []

    #loop through all hashtags and get data
    for document in out:
        tempPostIds = []
    
        #check if it has next page
        hasNextPage = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["page_info"]["has_next_page"]
        hashtag = document["data"]["hashtag"]["name"]
        next_cursor = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["page_info"]["end_cursor"]

        next_cursor_array = []
        next_cursor_array.append(next_cursor)

        #get posts and loop through to get post ids

        posts = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["edges"]
        for doc in posts:
            postId = doc["node"]["shortcode"]
            temp = [postId, hashtag]
            tempPostIds.append(temp)
        if hasNextPage:
            count = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["count"]
            print(count)
            time.sleep(3)
            tenmpPostIds = []
            next_cursor =""
            tempPostIds = getHashTagWhileLoop(hashtag, tempPostIds, next_cursor_array, count)
            print(len(tempPostIds[0]))

        post_ids.append(tempPostIds)


            

        if hasNextPage:
            end_cursor = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["page_info"]["end_cursor"]



    return post_ids