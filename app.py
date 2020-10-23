import os
import requests
from flask import Flask, request, jsonify, url_for, session, escape
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.secret_key = 'eCommerce'

app.config ["MONGO_DBNAME"] = "eCommerce_shop"
app.config["MONGO_URI"] = "mongodb+srv://khaled:sabrina03282016@cluster0.7kuww.mongodb.net/eCommerce_shop?retryWrites=true&w=majority"
mongo = PyMongo(app)



@app.route('/')
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return f'''('<pre>' + r.text + '</pre>')'''

@app.route('/get', methods=["GET"])
def get_products ():
     products = mongo.db.products

     output = []

     for product in products.find(): 
          
          output.append({'id': str(product['_id']),'Title': product['Title'], 'Category': product['Category'], 
          'Size':product['Size'],'Color': product['Color'],
          'Price':product['Price']})
          
          
    
     return  jsonify({"result": output})


if __name__ == '__main__': 
     app.run(debug=True)