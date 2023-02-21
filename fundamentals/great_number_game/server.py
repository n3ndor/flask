from flask import Flask, render_template,session, redirect
import random

app = Flask(__name__)

app.secret_key ="RunTimeError: The session is unavailable because no secret key was set."
#random.int(1,100) == random number between 1-100



@app.route("/")
def index():
    session["nr"] = random.randint(1,100)
    return render_template("index.html")



@app.route("/reset")
def new_game():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)