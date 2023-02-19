from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",row=8,col=8,color1="red",color2="black")

@app.route("/<int:x>")
def rows(x):
    return render_template("index.html",row=x,col=8,color1="red",color2="black")

@app.route("/<int:x>/<int:y>")
def col(x,y):
    return render_template("index.html",row=x,col=y,color1="red",color2="black")

@app.route("/<int:x>/<int:y>/<string:first>")
def color(x,y,first):
    return render_template("index.html",row=x,col=y,color1=first,color2="black")

@app.route("/<int:x>/<int:y>/<string:first>/<string:second>")
def all(x,y,first,second):
    return render_template("index.html",row=x,col=y,color1=first,color2=second)

if __name__ == "__main__":
    app.run(debug=True)