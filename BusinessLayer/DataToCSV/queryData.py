import sys, os
sys.path.append(os.path.abspath(os.path.join('../../..', 'WProjectSave')))
from db.Helpers.dbConnect import connect
from BusinessLayer.DataToCSV.dataToCSV import toDF


def QueryData():
    db = connect("WellsData")
    #This is where you set the date for have posted atleast once since this date

    cursor = db.Hashtags.find({})
    data = []
    for document in cursor:
        temp = [
        document["username"],
        document["profilepic_url"],
        document["followers"],
        document["linkToPost"],
        document["Description"],
        document["postComments"],
        document["postLikes"]]
        data.append(temp)
    
    toDF(data)

QueryData()
