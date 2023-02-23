from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key="we are going to be ninjas again"



@app.route("/")
def index():
    gold = 0
    return render_template("index.html", gold=gold)

@app.route("/process_money", methods=["POST"])
def calculating():
    
    
    return redirect("index.html")



if __name__ == "__main__":
    app.run(debug=True)