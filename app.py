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

@app.route('/add_recipe')
def add_recipe(): 
    return render_template("add-recipe.html", allergens=mongo.db.allergens.find(), lifestyle=mongo.db.lifestyle.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    form_data = request.form.copy()
    ingredients=[];
    instructions=[];
    allergens=[];
    for field in request.form:
        if field[:-1] == "ingredient":
            ingredients.append(form_data[field])
            del form_data[field]
        if field[:-1] == "instruction":
            instructions.append(form_data[field])
            del form_data[field]
        if field[:8] == "checkbox":
            allergens.append(field[8:])
            del form_data[field]
    
    if len(ingredients) > 0:
        form_data["ingredients"] = ingredients
    if len(instructions) > 0:
        form_data["instructions"] = instructions
    if len(allergens) > 0:
        form_data["allergens"] = allergens
    
    recipes = mongo.db.recipes
    recipes.insert_one(form_data.to_dict())
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_allergens = mongo.db.allergens.find()
    all_lifestyles = mongo.db.lifestyle.find()
    return render_template('edit-recipe.html', recipe=the_recipe, allergens=all_allergens, lifestyle=all_lifestyles, recipe_id=recipe_id)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    form_data = request.form.copy()
    ingredients=[];
    instructions=[];
    allergens=[];
    for field in request.form:
        if field[:-1] == "ingredient":
            ingredients.append(form_data[field])
            del form_data[field]
        if field[:-1] == "instruction":
            instructions.append(form_data[field])
            del form_data[field]
        if field[:8] == "checkbox":
            allergens.append(field[8:])
            del form_data[field]
    
    if len(ingredients) > 0:
        form_data["ingredients"] = ingredients
    if len(instructions) > 0:
        form_data["instructions"] = instructions
    if len(allergens) > 0:
        form_data["allergens"] = allergens
    
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(recipe_id)}, {
        'name': form_data['name'],
        'description': form_data['description'],
        'time': form_data['time'],
        'lifestyle': form_data['lifestyle'],
        'instructions': form_data['instructions'],
        'ingredients': form_data['ingredients'],
        'allergens': form_data['allergens']
    })
    return redirect(url_for('get_recipes'))
    
    
    

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipes = mongo.db.recipes
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipes.delete_one(the_recipe)
    return redirect(url_for('get_recipes'))
    
    
    
if __name__ == "__main__":
    app.run(host=os.getenv("IP"), 
    port=int(os.getenv("PORT")), 
    debug=True)
    
    