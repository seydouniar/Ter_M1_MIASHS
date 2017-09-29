#!/usr/bin/env python3
import pprint
import json
from bson.json_util import dumps
from pymongo import MongoClient
import codecs
client = MongoClient('mongodb://localhost:27017/')
db = client.dico
collection = db.dictionnaires

txt =codecs.open("2test.txt",'r','utf-8')
a=txt.read()
list_phrase=a.split(" ")
def def_word(mot):
	cols=collection.find({"M.mot":{"$regex":"^"+mot}})
	jobject = json.loads(dumps(cols))
	for i in range(len(jobject)):
		pprint.pprint(jobject[i]['M']['mot']+": "+jobject[i]['CA']['categorie']
			+", def: "+jobject[i]['SENS']+" dom" + jobject[i]['DOM']['nom']+
			", op: "+ jobject[i]['OP'])
for mot in list_phrase:
	def_word(mot)	
