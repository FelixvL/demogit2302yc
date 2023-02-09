from flask import Flask
import felix

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/ietskiezen")
def ietskiezen():
    getal = 5
    getal += 24
    print(getal)
    return "dit geef ik terug"+ str(getal)

@app.route("/felix/<zoekterm>")
def doorfelix(zoekterm):
    getal = 5
    getal += 24
    print(getal)
    return felix.eigenextramethode(zoekterm)

