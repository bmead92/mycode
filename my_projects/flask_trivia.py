#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

# route for correct answer
@app.route("/correct")
def success():
    return f"That is correct!"

# base route
@app.route("/")
def start():
    # return a trivia template
    return render_template("trivia_template.html")

# route for login
@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm") and request.form.get("nm") == "42":
                return redirect("/correct")
        else:
            return redirect("/")

# if run from this program, connect to the server and run app
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

