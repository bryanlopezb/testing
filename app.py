from flask import Flask, Response
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/catfact")
def catfact():

    url = "https://catfact.ninja/fact"
    r = requests.get(url)
    fact = r.json()
    #print to console
    print("Did you know?: \n")
    print(fact)
    

    return Response(json.dumps(fact))

if __name__ == '__main__':
    app.run()
