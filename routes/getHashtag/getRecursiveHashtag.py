from pymongo import MongoClient
#import sys, os
import time
import concurrent.futures
import requests
from decouple import config


def getHashTagWhileLoop(hashtag, shortcodes, next_cursor, count):
    querystrings = []
    out = []
    counter = 0
     
            

    url = config("API_URL2")+"/tag/"+hashtag+"/feed"


    headers = {
        'x-rapidapi-key': config("API_KEY2"),
        'x-rapidapi-host': config("API_HOST2")
        }





    def load_url2(hashtag, next_cursor):
        url = config("API_URL")+"/hash_tag_medias"


        headers = {
            'x-rapidapi-key': config("API_KEY"),
            'x-rapidapi-host': config("API_HOST")
            }
        response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag, "next_cursor": next_cursor},)
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag})
        return response.json()

    def load_url(next_cursor):
        response = requests.request("GET", url, headers=headers, params={"pageId": next_cursor})
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params={"pageId": next_cursor})
        return response.json()


    document = load_url2(hashtag, next_cursor[-1])
    next_cursor_array =  []
    #print(document)
    print("*****!!!!!*****\n\n\n\n\n")
    print(count)
    print("*****!!!!!*****\n\n\n\n\n\n\n")

    num = 2
    while document['data']["hashtag"]["edge_hashtag_to_media"]["page_info"]["end_cursor"] is not None:
        #print("PAID FOR")
        posts = document['data']["hashtag"]["edge_hashtag_to_media"]["edges"]
        hashtag = document["data"]["hashtag"]["name"]
        next_cursor = document['data']["hashtag"]["edge_hashtag_to_media"]["page_info"]["end_cursor"]
        #print(next_cursor)
        next_cursor_array.append(next_cursor)
        for doc in posts:
            postId = doc["node"]["shortcode"]
            temp = [postId, hashtag]
            if temp not in shortcodes:
                shortcodes.append(temp)

            
        print(len(shortcodes))
        #print("NEXTCURSOR!!!")
        #print(next_cursor)
        document = load_url2(hashtag, next_cursor_array[-1])
    print("DONE")
    print(len(shortcodes))
    time.sleep(5)
    #print(shortcodes)
    print(len(shortcodes))
    return shortcodes








"""
  
def getHashTagWhileLoop(hashtag, shortcodes, next_cursor):
    querystrings = []
    out = []
    counter = 0
     
            

    url = config("API_URL2")+"/tag/"+hashtag+"/feed"


    headers = {
        'x-rapidapi-key': config("API_KEY2"),
        'x-rapidapi-host': config("API_HOST2")
        }



    def load_url(next_cursor):
        response = requests.request("GET", url, headers=headers, params={"pageId": next_cursor})
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params={"pageId": next_cursor})
        return response.json()


    document = load_url(next_cursor)
    
    while document['meta']["next_page"] is not None:
        posts = document['data']
        next_cursor = document['meta']["next_page"]
        print(next_cursor)
        for doc in posts:
            postId = doc["short_code"]
            temp = [postId, hashtag]
            shortcodes.append(temp)
        print(len(shortcodes))
        print("NEXTCURSOR!!!")
        print(next_cursor)
        document = load_url(next_cursor)
        print(document['meta'])
        time.sleep(3)
    print("DONE")
    print(len(shortcodes))
    time.sleep(100)
    print(shortcodes)
    print(len(shortcodes))
    return shortcodes
"""










"""
from pymongo import MongoClient
#import sys, os
import time
import concurrent.futures
import requests
from decouple import config

    
def getHashTagWhileLoop(hashtag, shortcodes, next_cursor):
    querystrings = []
    out = []
    counter = 0
     
            

    url = config("API_URL2")+"/tag/"+hashtag+"/feed"


    headers = {
        'x-rapidapi-key': config("API_KEY2"),
        'x-rapidapi-host': config("API_HOST2")
        }



    def load_url(hashtag, next_cursor):
        response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag, "next_cursor": next_cursor},)
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag})
        return response.json()


    document = load_url(hashtag, next_cursor)
    hasNextPage = document['data']["hashtag"]["edge_hashtag_to_media"]["page_info"]["has_next_page"]
    print(hasNextPage)

    while document['data']["hashtag"]["edge_hashtag_to_media"]["page_info"]["end_cursor"] is not None:
        posts = document['data']["hashtag"]["edge_hashtag_to_media"]["edges"]
        hashtag = document["data"]["hashtag"]["name"]
        next_cursor = document['data']["hashtag"]["edge_hashtag_to_media"]["page_info"]["end_cursor"]
        print(next_cursor)
        for doc in posts:
            postId = doc["node"]["shortcode"]
            temp = [postId, hashtag]
            shortcodes.append(temp)
            print(len(shortcodes))
        document = load_url(hashtag, next_cursor)
        time.sleep(5)
    time.sleep(100)
    print(shortcodes)
    print(len(shortcodes))
    return shortcodes
"""
"""
from pymongo import MongoClient
#import sys, os
import time
import concurrent.futures
import requests
from decouple import config

"""
"""

def getHashTagWhileLoop(hashtag, shortcodes, next_cursor, count):
    querystrings = []
    out = []
    counter = 0
     
            
    url = config("API_URL")+"/hash_tag_medias_v2"


    headers = {
        'x-rapidapi-key': config("API_KEY"),
        'x-rapidapi-host': config("API_HOST")
        }




    def load_url(hashtag, next_cursor):
        response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag, "next_cursor": next_cursor},)
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag})
        return response.json()


    document = load_url(hashtag, next_cursor[-1])
    print("**************\n\n\n\n\n\n")
    print(count)
    print("**************\n\n\n\n\n\n")
    hasNextPage = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["page_info"]["has_next_page"]
    print(hasNextPage)
    next_cursor_array =  []
    while document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["page_info"]["end_cursor"] is not None:
        posts = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["edges"]
        hashtag = document["data"]["hashtag"]["name"]
        next_cursor = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["page_info"]["end_cursor"]
        #next_cursor = next_cursor.replace('==', '')
        print(next_cursor)
        next_cursor_array.append(next_cursor)
        for doc in posts:
            postId = doc["node"]["shortcode"]
            temp = [postId, hashtag]
            if temp not in shortcodes:
                shortcodes.append(temp)
  
            
        print(len(shortcodes))
        print("NEXTCURSOR!!!")
        print(next_cursor)
        document = load_url(hashtag, next_cursor_array[-1])
        #if document['data']["hashtag"]["edge_hashtag_to_media"]["page_info"]["end_cursor"] is None:
            #getHashTagWhileLoop2(hashtag, shortcodes, next_cursor, count)
            #document = load_url(hashtag, next_cursor_array)
            


        #time.sleep()
    print("DONE")
    time.sleep(10)
    print(shortcodes)
    print(len(shortcodes))
    return shortcodes

"""

def getHashTagWhileLoop3(hashtag, shortcodes, next_cursor, count):
    querystrings = []
    out = []
    counter = 0
     
            
    url = config("API_URL3")+"/clients/api/ig/media_by_tag"


    headers = {
        'x-rapidapi-key': config("API_KEY3"),
        'x-rapidapi-host': config("API_HOST3")
        }


    next_cursor_array = []

    def load_urlrecent(hashtag, next_cursor):
        response = requests.request("GET", url, headers=headers, params={"tag":hashtag,"feed_type":"recent","corsEnabled":"true", "nextMaxId":next_cursor})
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(40)
            response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag})
        return response.json()
    def load_urltop(hashtag, next_cursor):
        response = requests.request("GET", url, headers=headers, params={"tag":hashtag,"feed_type":"top","corsEnabled":"true", "nextMaxId":next_cursor})
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(40)
            response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag})
        return response.json()
    def load_urlreels(hashtag, next_cursor):
        response = requests.request("GET", url, headers=headers, params={"tag":hashtag,"feed_type":"reels","corsEnabled":"true", "nextMaxId":next_cursor})
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(40)
            response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag})
        return response.json()
    
    document = load_urlrecent(hashtag, next_cursor[-1])
    print("**************\n\n\n\n\n\n")
    print(count)
    print("**************\n\n\n\n\n\n")
    #hasNextPage = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["page_info"]["has_next_page"]
    #print(hasNextPage)
    next_cursor_array =  []
    while document["moreAvailable"] is not False:
        posts = document['data']
        next_cursor = document["nextMaxId"]

        print(next_cursor)
        next_cursor_array.append(next_cursor)
        for doc in posts:
            postId = doc["code"]
            temp = [postId, hashtag]
            if temp not in shortcodes:
                shortcodes.append(temp)
  
            
        print(len(shortcodes))
        print("NEXTCURSOR!!!")
        print(next_cursor)
        time.sleep(20)
        document = load_urlrecent(hashtag, next_cursor_array[-1])
        try:
            print(document["moreAvailable"])
        except:
            break
        #if document["moreAvailable"] == False:
            #break
        


        #time.sleep()
    
    time.sleep(20)
    
    document = load_urltop(hashtag, "")
    posts = document['data']
    next_cursor = document["nextMaxId"]

    
    print(next_cursor)
    next_cursor_array.append(next_cursor)
    for doc in posts:
        try:
            #print(doc)
            postId = doc["code"]
            temp = [postId, hashtag]
            if temp not in shortcodes:
                shortcodes.append(temp)
        except:
            nan = 0

    while document["moreAvailable"] is not False:
        posts = document['data']
        next_cursor = document["nextMaxId"]

        print(next_cursor)
        next_cursor_array.append(next_cursor)
        for doc in posts:
            try:
                postId = doc["code"]
                temp = [postId, hashtag]
                if temp not in shortcodes:
                    shortcodes.append(temp)
            except:
                nan = 0

  
            
        print(len(shortcodes))
        print("NEXTCURSOR!!!")
        print(next_cursor)
        time.sleep(20)
        document = load_urltop(hashtag, next_cursor_array[-1])
        try:
            print(document["moreAvailable"])
        except:
            break
        #if document["moreAvailable"] == False:
            #break
        


        #time.sleep()
    """
    time.sleep(20)
    document = load_urlreels(hashtag, "")
    posts = document['data']
    next_cursor = document["nextMaxId"]

    print(next_cursor)
    next_cursor_array.append(next_cursor)
    for doc in posts:
        postId = doc["code"]
        temp = [postId, hashtag]
        if temp not in shortcodes:
            shortcodes.append(temp)

    while document["moreAvailable"] is not False:
        posts = document['data']
        next_cursor = document["nextMaxId"]

        print(next_cursor)
        next_cursor_array.append(next_cursor)
        for doc in posts:
            postId = doc["code"]
            temp = [postId, hashtag]
            if temp not in shortcodes:
                shortcodes.append(temp)
  
            
        print(len(shortcodes))
        print("NEXTCURSOR!!!")
        print(next_cursor)
        time.sleep(20)
        document = load_urlrecent(hashtag, next_cursor_array[-1])
        try:
            print(document["moreAvailable"])
        except:
            break
        #if document["moreAvailable"] == False:
            #break
        


        #time.sleep()
    """
    print("DONE")
    time.sleep(10)
    print(shortcodes)
    print(len(shortcodes))
    return shortcodes
    

"""

end_cursors = ["QVFBdjRONFNWc1RTT0kzR1VTZ0pYLWtwSWNoaHF5QkJuekpHQ2lPQTFUMTQyNmlCMzdyVzRudmtKZi1JSjBYd3hxeXFHVnJmOGx4TmNsSThpTFhzMExUMQ",]
def getHashTagWhileLoop(hashtag, shortcodes, next_cursor, count):
    querystrings = []
    out = []
    counter = 0
     
            
    url = config("API_URL4")+"hashtag/feed"


    headers = {
        'x-rapidapi-key': config("API_KEY4"),
        'x-rapidapi-host': config("API_HOST4")
        }




    def load_url(hashtag, next_cursor):
        response = requests.request("GET", url, headers=headers, params={"hashtag": hashtag,
    "end_cursor": next_cursor})
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(120)
            response = requests.request("GET", url, headers=headers, params={"hash_tag":hashtag})
        return response.json()


    document = load_url(hashtag, next_cursor[-1])
    print("**************\n\n\n\n\n\n")
    print(count)
    print("**************\n\n\n\n\n\n")
    #hasNextPage = document['data']["hashtag"]["edge_hashtag_to_ranked_media"]["page_info"]["has_next_page"]
    #print(hasNextPage)
    next_cursor_array =  []
    while document["end_cursor"] is not None:
        posts = document['collector']
        next_cursor = document["end_cursor"]

        print(next_cursor)
        next_cursor_array.append(next_cursor)
        for doc in posts:
            postId = doc["shortcode"]
            temp = [postId, hashtag]
            if temp not in shortcodes:
                shortcodes.append(temp)
  
            
        print(len(shortcodes))
        print("NEXTCURSOR!!!")
        print(next_cursor)
        time.sleep(10)
        document = load_url(hashtag, next_cursor_array[-1])
        try: 
            print(document["end_cursor"])
        except:
            print(document)
            time.sleep(5)
            document = load_url(hashtag, next_cursor_array[-3])
            next_cursor_array.pop()

        #if document['data']["hashtag"]["edge_hashtag_to_media"]["page_info"]["end_cursor"] is None:
            #getHashTagWhileLoop2(hashtag, shortcodes, next_cursor, count)
            #document = load_url(hashtag, next_cursor_array)
            


        #time.sleep()
    print("DONE")
    time.sleep(10)
    print(shortcodes)
    print(len(shortcodes))
    return shortcodes
"""
