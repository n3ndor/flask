from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

app.secret_key ="RunTimeError: The session is unavailable because no secret key was set."
#random.int(1,100) == random number between 1-100

@app.route("/")
def index():
    answer="your guess"
    session["nr"] = random.randint(1,100)
    return render_template("index.html")

@app.route("/reset")
def new_game():
    session.clear()
    return redirect("/")

@app.route("/guess", methods=["post"])
def guess():
    if int(request.form["nr"]) == int(session["nr"]):
        answer = "you are Correct"
        return render_template("index.html", answer = answer)
    elif int(request.form["nr"]) < int(session["nr"]):
        answer = "too low, go higher"
        return render_template("index.html", answer = answer)
    else:
        answer = "too high, go lower"
        return render_template("index.html", answer = answer)


    # session["submit"] = int(request.form["submit"])
    # return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)