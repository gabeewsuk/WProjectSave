from pymongo import MongoClient
import sys, os
import time
import concurrent.futures
import requests
from decouple import config
#import sys, os
sys.path.append(os.path.abspath(os.path.join('../../..', 'WellsSoftware')))
from db.findNUpdate.findAndUpdate import findAndUpdatePost
from db.Helpers.dbConnect import connect

#from Folder.db.Finders.dbFindUserNames import findUserNames




#getUserId from an array of usernames
def getPostStats(post_ids):
    subset = []
    

    querystrings = []
    out = []
    counter = 0
    print(post_ids)

     
            

    url = config("API_URL")+"/media_info"


    headers = {
        'x-rapidapi-key': config("API_KEY"),
        'x-rapidapi-host': config("API_HOST")
        }



    def load_url(id):
        response = requests.request("GET", url, headers=headers, params={"short_code":id})
        print(id)
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params={"short_code":id})
        return response.json()

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = (executor.submit(load_url, id)for id in post_ids)
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
    posts = []

    #loop through all hashtags and get data
    for document in out:
        
        tempPostData = []
        username = document['data']['shortcode_media']['owner']['username']
        followers = document['data']['shortcode_media']['owner']['edge_followed_by']['count']
        profilePic = document['data']['shortcode_media']['owner']['profile_pic_url']

        #Post Data
        post_comments = document['data']['shortcode_media']["edge_media_to_comment"]["count"]
        post_likes = document['data']['shortcode_media']["edge_media_preview_like"]["count"]
        code = document['data']['shortcode_media']["shortcode"]
        link_to_post = "https://www.instagram.com/p/"+code+"/"
        caption = document['data']['shortcode_media']["edge_media_to_caption"]["edges"][0]["node"]["text"]
        #adding each post id in with corresponding hashtag to dictionary
       
        tempPostData.append(username)
        tempPostData.append(followers)
        tempPostData.append(profilePic)
        tempPostData.append(post_comments)
        tempPostData.append(post_likes)      
        tempPostData.append(link_to_post)
        tempPostData.append(caption)
        posts.append(tempPostData)



                

 
        #except Exception as exc:
            #print("!!!!!!getUserPostData.py!!!!!")
            #print(exc)
	        # handle the error 
    
    

    return posts
