'''
Backend server for Avocado - HackNY 2019 
'''

# Flask Imports
import flask
from flask import request

# Firebase Imports
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

# Python Import
import requests
import json

# Starting Up

app = flask.Flask(__name__)

cred = credentials.Certificate(
    "tofu-hack-firebase-adminsdk-c151z-fe8bbb6fc3.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tofu-hack.firebaseio.com/'
})

RESTAURANTS = db.reference('restaurants')
FOODIES = db.reference('foodies')
CHEFS = db.reference('chefs')
RSVP = db.reference('RSVP')
MATCHED = db.reference('matched')

########### RESTAURANT FUNCTIONS ##############


@app.route("/get-restaurant-data", methods=['POST'])
def getRestaurantData():
    RestID = request.json['RestID']
    response = RESTAURANTS.order_by_child('RestID').equal_to(RestID).get()
    for key, value in response.items():
        print(key)
        print(value)
    return(value)

@app.route("/get-all-restaurants", methods=['GET'])
def getAllRestaurants():
    rest_list = RESTAURANTS.get()
    rlist= []
    for key in rest_list:
        rlist.append(rest_list[key])
    rdict = {
        '0': rlist
    }

    return rdict

@app.route("/create-restaurant", methods=['POST'])
def createRestaurant():
    RestID = request.json['RestID']
    Name = request.json['Name']
    Cuisine = request.json['Cuisine']
    History = request.json['History']
    Occ_Limit = request.json['Occupancy Limit']
    Open_Sch = request.json['Open Schedule']
    Rent_Rate = request.json['Rental Rate']
    Position = request.json['position']


    payload = {
        "Cuisine": Cuisine,
        "History" : History,
        "Name" : Name,
        "Occupancy Limit" : Occ_Limit,
        "Open Schedule" : Open_Sch,
        "Rental Rate" : Rent_Rate,
        "RestID" : RestID,
        "position": Position
    }

    restaurant = RESTAURANTS.push(payload)
    return(RestID)

########### END OF RESTAURANT FUNCTIONS ###########


########## CHEF FUCTIONS #######################
@app.route("/get-chef-data", methods=['POST'])
def getChefData():
    ChefID = request.json['ChefID'] 
    response = CHEFS.order_by_child('ChefID').equal_to(ChefID).get()
    for key, value in response.items():
        print(value)
    return(value)

########### END OF CHEF FUNCTIONS ###########


########## FOODIE FUCTIONS #######################
@app.route("/get-foodie-data", methods=['POST'])
def getFoodieData():
    FoodieID = request.json['CustID'] 
    response = FOODIES.order_by_child('CustID').equal_to(FoodieID).get()
    for key, value in response.items():
        print(value)
    return(value)
<<<<<<< HEAD

@app.route("/add-favorite", methods=['POST'])
def addFavorite():
    favorite_chef = request.json['ChefID']
    foodieID = request.json['CustID']
    foodie = FOODIES.order_by_child('CustID').equal_to(foodieID).get()
    print(foodie)
    foodie['1']['Favorites'].append(favorite_chef)
    FOODIES.update({
        '1': foodie['1']
    })
    # print("running add favorite")
    # print(type(FOODIES.child))
    return favorite_chef


=======
    
>>>>>>> e3c99941c3833cf82e87eb611373e957bc2736ee
########### END OF FOODIE FUNCTIONS ###########


########## GOOGLE MAPS FUNCTIONS #######################

########### END OF GOOGLE MAPS FUNCTIONS ###########


########## MISC FUCTIONS #######################
@app.route("/create-match", methods=['POST'])
def createMatch():
    match = request.json
    print(type(match))
    create_match = MATCHED.push(match)
    return create_match

########### END OF MISC FUNCTIONS ###########
