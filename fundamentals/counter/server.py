from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key="top secret app key"


@app.route("/")
def index():
    if "count" and "visited" not in session:
        session["count"] = 0
        session["visited"] = 0
        session["increment"] = 2
    else:
        session["visited"] += 1
    return render_template("index.html")

@app.route("/add")
def add():
    session['count'] += session["increment"]
    return redirect("/")


@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")

# #add a specific number for multiplying
# @app.route("/count/<int:n>")
# def add_n(n):
#     session['count'] += n
#     return render_template("index.html")

@app.route("/increment", methods=["post"])
def set_increment_value():
    session["count"] += int(request.form["increment"])
    session["increment"] = int(request.form["increment"])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)