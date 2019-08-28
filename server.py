import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html");

@app.route('/save_the_sea')
def save_the_sea():
    return render_template("/save_the_sea/save_the_sea.html");

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
