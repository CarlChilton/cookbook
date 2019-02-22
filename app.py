import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(host=os.getenv("IP"), 
    port=int(os.getenv("PORT")), 
    debug=True)
    
    