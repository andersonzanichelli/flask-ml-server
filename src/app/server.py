from flask import Flask
from flask import request
from logging.config import dictConfig
import logging

from service import Service

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

logging.getLogger("mylogger")

app = Flask(__name__)

species = { 0: "Iris setosa", 1: "Iris versicolor", 2: "Iris virginica" }

@app.get("/predict")
def predict():
    logging.info(f'Received request to predict. Request: {request}')

    model = "src/data_science/iris.knn.model"
    result = Service(model).execute(request)

    resp = {
            "model": model,
            "prediction": str(result),
            "name": species[result[0]]
            }

    logging.info(f'Response with prediction: {resp}')

    return resp