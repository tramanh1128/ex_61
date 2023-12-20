from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():
    return "Index Page"



if __name__ == '__main__':
    app.run(debug=True)
