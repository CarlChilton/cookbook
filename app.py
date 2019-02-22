import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "recipes"
app.config["MONGO_URI"] = "mongodb://admin:password1@ds147225.mlab.com:47225/recipes"

mongo = PyMongo(app)

@app.route("/")
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())


if __name__ == "__main__":
    app.run(host=os.getenv("IP"), 
    port=int(os.getenv("PORT")), 
    debug=True)
    
    