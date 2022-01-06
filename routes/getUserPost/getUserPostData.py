from pymongo import MongoClient
import sys, os
import time
import concurrent.futures
import requests
from decouple import config
#import sys, os
sys.path.append(os.path.abspath(os.path.join('../../..', 'WellsSoftware')))
from db.findNUpdate.findAndUpdate import findAndUpdatePost
from routes.getUserPost.queryData import VerifyLead
from db.Helpers.dbConnect import connect
from datetime import datetime
from db.Helpers.dbConnect import connect


#from Folder.db.Finders.dbFindUserNames import findUserNames




#getUserId from an array of usernames
def getPostStats(post_ids):
    db = connect('WellsData')
    subset = []
    hashtag = post_ids[0][1]

    querystrings = []
    out = []
    counter = 0
    VerifiedLeads = []
    #print(post_ids)

     
            

    url = config("API_URL")+"/media_info"


    headers = {
        'x-rapidapi-key': config("API_KEY"),
        'x-rapidapi-host': config("API_HOST")
        }



    def load_url(id):
        id = id[0]
        response = requests.request("GET", url, headers=headers, params={"short_code":id})
        print("ID:")
        print(id)
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params={"short_code":id})
        return response.json()
    for id in post_ids:
        if VerifiedLeads.length() <=10:
            break
        else:
            document = load_url(id)
            
            try:
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
                timestamp = document["data"]["shortcode_media"]["taken_at_timestamp"]
                date = datetime.fromtimestamp(timestamp)
                postPic = document["data"]["shortcode_media"]["display_url"]


                #add hashtag
                #adding each post id in with corresponding hashtag to dictionary
            
                tempPostData.append(username)
                tempPostData.append(followers)
                tempPostData.append(profilePic)
                tempPostData.append(post_comments)
                tempPostData.append(post_likes)      
                tempPostData.append(link_to_post)
                tempPostData.append(caption)
                tempPostData.append(hashtag)
                tempPostData.append(date)
                tempPostData.append(postPic)
                if VerifyLead(temPostData) == True:
                    VerifiedLeads.append(tempPostData)
                    findAndUpdatePost(db, tempPostData)
                else:
                    pass            
       

                

        
        

            
        except Exception as exc:
            #print(document)
            #print(exc)
            print("!!!!!!GETUSERPOSTDATA.py!!!!!!")
            time.sleep(10)



                

 
       
    
    

    return VerifiedLeads
