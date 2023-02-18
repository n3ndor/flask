from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def say(name):
    return "Hi " + name + "!"

@app.route("/repeat/<int:nr>/<string:text>")
def repeat(nr,text):
    return f"<p>{text}</p>" * nr

@app.route("/<random>")
def random_text(random):
    return "You are not allowed to access this Site, return immediately<br>or i will call the cops<br>piu-piu, bang-bang"

if __name__=="__main__":
    app.run(debug=True)

