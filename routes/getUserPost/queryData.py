import sys, os
sys.path.append(os.path.abspath(os.path.join('../../..', 'WProjectSave')))
from db.Helpers.dbConnect import connect
from BusinessLayer.DataToCSV.dataToCSV import toDF


VerifyLead(document)
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
        return True
    else:
        return False