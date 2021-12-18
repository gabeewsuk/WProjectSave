import pandas as pd
 

def toDF(data):
    df = pd.DataFrame(data, columns = ['username', 'profilepic', 'followers', 'Link', 'caption', 'comments', 'likes'])
    df.to_csv('output.csv', index = False, header = True)