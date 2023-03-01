from pymongo import MongoClient
import ssl
from core import config

ssl._create_default_https_context = ssl._create_unverified_context



# client = MongoClient("mongodb+srv://adminjame:1234@cluster0.4ientud.mongodb.net/?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

# client = MongoClient("mongodb+srv://"+config.settings.user_name+":"+config.settings.pass_word+"@"+config.settings.host+"/?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
client = MongoClient("mongodb+srv://"+config.settings.user_name+":"+config.settings.pass_word+"@"+config.settings.host+"/test", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db = client.swe_classroom

collection_name = db["course"]
