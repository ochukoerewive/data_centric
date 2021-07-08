import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello world again!!!"

if __name__ == "__main__":
   app.run(clear
   pipdebug=True)