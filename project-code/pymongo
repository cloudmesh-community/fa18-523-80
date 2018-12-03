import pymongo
import pandas as pd

client = pymongo.MongoClient('mongodb+srv://I523Admin:<I523Admin>@i523breastcancer-fdclg.mongodb.net/test?retryWrites=true')

db = client['Wisconsin_Breast_Cancer']

collection = db['I523']

df = pd.DataFrame(list(collection.find()))
