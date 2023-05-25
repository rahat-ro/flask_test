import json
from flask import Flask, Response, request, jsonify
from bson import json_util, ObjectId
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)

app.config[
    "MONGO_URI"] = "mongodb+srv://chainAI:chain.ai@clusterrevenuechain.wi8m2.mongodb.net/merchant?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return str("hello")

@app.route("/fetch/merchant/profile", methods=["GET"])
def fetchMerchantProfile():
    data = mongo.db.users

    output = []

    for q in data.find():
        output.append({"mobNo": q["mobNo"],
                       "nidNo": q["nidNo"],
                       "shopName": q["shopName"],
                       "licenseNo": q["licenseNo"],
                       "walletId": q["walletId"],
                       "vatWalletId": q["vatWalletId"],
                       "shopIdentity": q["shopIdentity"],
                       "serviceCode": q["serviceCode"],
                       "serviceName": q["serviceName"],
                       "vatRate": q["vatRate"],
                       })

    return output


if __name__ == '__main__':
    app.run()
