from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)

app.secret_key="we are going to be ninjas again"

@app.route("/")
def index():
    gold = 0
    if "gold" not in session:
        session["gold"] = 0

    return render_template("index.html", gold=gold)

@app.route("/process_money", methods=["POST"])
def calculating():
    
    print(session["gold"])
    return redirect("index.html")
    
    # return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)