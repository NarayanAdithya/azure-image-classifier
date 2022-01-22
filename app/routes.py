from app import app
from flask import render_template, request
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": app.config['KEY']})
predictor = CustomVisionPredictionClient(app.config['ENDPOINT'], prediction_credentials)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.files['Image'])
        if request.files['Image']:
            results = predictor.classify_image(app.config['PROJECT_ID'], app.config['PUBLISH_ITERATION_NAME'], request.files["Image"].read())
            perc=results.predictions[0].probability
            tag=results.predictions[0].tag_name
        return render_template('home.html',perc=round(perc*100,3),tag=tag)
    return render_template('home.html',perc='',tag='')

@app.route('/learn',methods=['GET'])
def learn():
    return render_template('learn.html')