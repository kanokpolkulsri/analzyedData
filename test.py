import pymongo
import pprint
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db4 = client['human']['each']

for data in db4.find().limit(50):
    print(',"'+data['name']+'"')