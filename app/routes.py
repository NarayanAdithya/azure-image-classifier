from app import app
from flask import render_template, request


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.files['Image'])

    return render_template('home.html')
