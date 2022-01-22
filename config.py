import os

class Config():
    SECRET_KEY = 'wIUGUDT%*&()*&(*TFG^*IT'
    PROJECT_ID = os.environ.get('PROJECT_ID')
    KEY = os.environ.get('KEY')
    ENDPOINT = os.environ.get('ENDPOINT')
    PUBLISH_ITERATION_NAME = os.environ.get('PUBLISH_ITERATION_NAME')