from flask import Flask,request
from flask import jsonify,request
from pymongo import MongoClient
from flask_cors import CORS


client = MongoClient('localhost', 27017) 
db = client.fpd   
todos = db.statusfeeDetails 

app = Flask(__name__)
title = "Flask+Mongo"
cors = CORS(app)

@app.route("/")
def redirect_url():
	return "Hello"

@app.route('/addCatTier', methods=['POST','GET'])
def addCatTier():
	addCat = db.catTier
	values = request.json
	print(values)
	for i in values:
		addCat.insert({ "llimit":i['llimit'], "ulimit":i['ulimit'], "sku":i['sku']})	
	return "Success"

@app.route('/getCatTier',methods=['GET'])
def getCatTierData():
	users = db.catTier.find()
	data = []
	for user in users:
		data.append({'llimit':user['llimit'],'ulimit':user['ulimit'],'sku':user['sku']})
		
	return jsonify(data)

@app.route('/getDetails',methods=['GET'])
def getDetails():
	users = db.details.find()
	data = []
	for user in users:
		data.append({'clientName':user['clientName'],'clientFeesOwner':user['clientFeesOwner'],'email':user['email'],\
		'secondaryEmail':user['secondaryEmail'],'createdBy':user['createdBy'],\
		'modifiedBy':user['modifiedBy'],'currency':user['currency'],'emailOptOut':user['emailOptOut'],\
		'carrierID':user['carrierID'],'exchangeRate':user['exchangeRate']})
		
	return jsonify(data)

@app.route('/getTier',methods=['GET'])
def getTierData():
	users = db.tier.find()
	data = []
	for user in users:
		data.append({'llimit':user['llimit'],'ulimit':user['ulimit'],'sku':user['sku']})
		
	return jsonify(data)


@app.route('/addTier', methods=['POST','GET'])
def addTier():
	addTier = db.tier
	values = request.json
	print(values[0])
	for i in values:
		addTier.insert({ "llimit":i['llimit'], "ulimit":i['ulimit'], "sku":i['sku']})
	return "Success"

@app.route("/update", methods=['POST','GET'])
def updateDetails ():
	users = db.details
	values = request.json
	print(values)
	

	itm = db.details.find_one({})
	print (itm.get('_id'))

	users.update({"_id":itm.get('_id')},
	 	{
		 '$set':{
			'clientName':values['name'],
			'clientFeesOwner':values['feesowner'],
			'email':values['email'],
			'secondaryEmail':values['semail'],
			'createdBy':values['created'],
			'modifiedBy':values['modified'],
			'currency':values['currency'],
			'emailOptOut':values['emailOpt'],
			'carrierID':values['carrier'],
			'exchangeRate':values['exchange']
			}
		}
	)

	
	return "Updated"



@app.route('/getClients',methods=['GET'])
def getClients():
	users = db.clients.find()
	data = []
	for user in users:
		data.append({'name':user['name']})
		
	return jsonify(data)

@app.route('/addClients', methods=['POST','GET'])
def addclient():
	addCat = db.clients
	values = request.json
	print(values)
	addCat.insert({ "name":values['name']})
	return jsonify(values)

if __name__ == "__main__":
	app.run(debug=True)



