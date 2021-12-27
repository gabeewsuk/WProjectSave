import sys, os
sys.path.append(os.path.abspath(os.path.join('../../..', 'WProjectSave')))
from db.Helpers.dbConnect import connect
from BusinessLayer.DataToCSV.dataToCSV import toDF


def QueryData(hashtag):
    db = connect("WellsData")
    #This is where you set the date for have posted atleast once since this date

    cursor = db.Hashtags.find({"hashtag":hashtag})
    data = []
    tier2check  = ["paid", "partner", "partnered", "ad", "advertisement", "sponsorship", "sponsor"]
    tier = "NONE"
    test1 = 0
    test2 = 0
    test3 = 0
    test4 = 0
    test5 = 0
    test7 = 0
    test6 = 0
    tier_1_words = ["gift", "#gift", " #pr ", " pr "]
    for document in cursor:
        test2+=1
        tier = False
            
        tier_2_words = [" ad ", "ad ", "#ad", "[ad]", "sponsored", "#sponsored", "#paid", "paid", "partner", "#partner", "partnered","#partnered"]
    
        for x in tier_2_words:
            if x in document["Description"].lower():
                tier = True
        for x in tier_2_words:
            if x in document["Description"].lower():
                tier = True

        if document["followers"] < 3000:
            #print("HERE")
            tier = False
            test4+=1
        for y in tier_1_words:
            if y in document["Description"].lower():
                tier = False
        if document["followers"] > 100000:
            tier = True
            test1 +=1
        for y in tier_1_words:
                if y in document["Description"].lower():
                    tier = False
        
        if tier == True:
            for y in tier_1_words:
                if y in document["Description"].lower():
                    print("Fucking up")
            test6+=1
            ER = round((int(document["postLikes"])/int(document["followers"])),4)
            ER = ER*100
            try:
                temp = [
                document["username"],
                document["profilepic_url"],
                document["followers"],
                document["linkToPost"],
                document["Description"],
                document["postComments"],
                document["postLikes"],
                document["hashtag"],
                document["date"],
                document["postPic"],
                ER,
                tier]
                data.append(temp)
            except:
                pass
        else:
            nan = 0
        tier = "NONE"
    print(test6)
    print("YOo")
    print(test1)
    print(test2)
    print(test3)
    print(test4)
    print(test5)
    #print(test6)
    toDF(data)

#QueryData()
