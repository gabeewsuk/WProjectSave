import pandas as pd
 

def toDF(data):
    df = pd.DataFrame(data, columns = ['username', 'profilepic', 'followers', 'Link', 'caption', 'comments', 'likes', "hashtag","date","profilePic","Engagement %", "tier"])
    df.to_csv('output2.csv', index = False, header = True)
    print("done updating data!")