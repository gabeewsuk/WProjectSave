from BusinessLayer.AddNewUsers.scrapeHashtag import newHashTag
from BusinessLayer.DataToCSV.queryData import QueryData
import time
from db.Helpers.dbConnect import connect

hashtag = "taimiapp"
hashtags = [hashtag]
newHashTag(hashtags)
#time.sleep(20)
#db = connect('WellsData')
#db.Hashtags.delete_many({"hashtag":"taimiapp"})
QueryData(hashtag)