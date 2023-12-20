from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():
    return "Index Page"

@app.route('/num_start')
def num_start():
    return render_template('plot.html')

@app.route('/numbers', methods=['POST'])
def numbers():
    toothpaste = request.form['ToothPaste']
    facecream = request.form['FaceCream']
    facewash = request.form['FaseWash']
    bathingsoap = request.form['BathingSoap']
    shampoo = request.form['Shampoo']
    moisturizer = request.form['Moisturizer']

    data = [float(toothpaste), float(facecream), float(facewash), float(bathingsoap), float(shampoo), float(moisturizer)]
    labels = ['ToothPaste', 'FaceCream', 'FaseWash', 'BathingSoap', 'Shampoo', 'Moisturizer']

    plt.clf()
    fig, ax = plt.subplots()
    pie = ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    
    plt.title('Distribution of Products')  # Added title
    
    # Add legend
    ax.legend(pie[0], labels, loc="upper left", bbox_to_anchor=(0.8, 0.5))
    
    fname = './static/piechart.jpg'
    plt.savefig(fname, bbox_inches='tight')
    
    return fname

if __name__ == '__main__':
    app.run(debug=True)
