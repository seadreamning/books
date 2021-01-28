from flask import Flask, render_template, request
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")