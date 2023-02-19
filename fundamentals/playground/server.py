from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("index.html", nr=3,color="powderblue")

@app.route("/play/<int:nr>")
def get_nr(nr):
    return render_template("index.html", nr=nr, color="powderblue")

@app.route("/play/<int:nr>/<string:color>")
def get_color(nr,color):
    return render_template("index.html", nr=nr,color=color)

if __name__ == "__main__":
    app.run(debug=True)