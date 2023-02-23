from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

app.secret_key ="RunTimeError: The session is unavailable because no secret key was set."
#random.int(1,100) == random number between 1-100

@app.route("/")
def index():
    answer = "your guess"
    again = " "
    session["nr"] = random.randint(1,100)
    print("session",session)
    return render_template("index.html")

@app.route("/reset")
def new_game():
    session.clear()
    return redirect("/")

@app.route("/guess", methods=["post"])
def guess():
    if int(request.form["nr"]) == int(session["nr"]):
        answer = "Your Guess is Correct, do you want to try again?"
        again = "<form action='/reset'><input class='again' type='submit' value='Start a New Game'></form>"
        return render_template("index.html", answer = answer, again=again)

    elif int(request.form["nr"]) < int(session["nr"]):
        answer = "Your Guess is too low, go higher"
        return render_template("index.html", answer = answer)

    else:
        answer = "Your Guess is too high, go lower"
        return render_template("index.html", answer = answer)


if __name__ == "__main__":
    app.run(debug=True)