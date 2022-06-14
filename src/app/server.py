from flask import Flask
from flask import request
from logging.config import dictConfig
from flask_expects_json import expects_json
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

schema = {
  "type": "object",
  "properties": {
    "sepal_length": { "type": "number" },
    "sepal_width": { "type": "number" },
    "petal_length": { "type": "number" },
    "petal_width": { "type": "number" }
  },
  "required": ["sepal_length", "sepal_width", "petal_length", "petal_width"]
}

@app.get("/predict")
@expects_json(schema)
def predict():
    logging.info(f'Received request to predict. Request: {request.json}')

    model = "src/data_science/iris.knn.model"
    result = Service(model).execute(request.json)

    resp = {
            "model": model,
            "prediction": str(result),
            "name": species[result[0]]
            }

    logging.info(f'Response with prediction: {resp}')

    return resp