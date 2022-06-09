from flask import Flask
from flask import request
from service import Service

app = Flask(__name__)

species = { 0: "Iris setosa", 1: "Iris versicolor", 2: "Iris virginica" }

@app.get("/predict")
def predict():
    model = "src/data_science/iris.knn.model"
    result = Service(model).execute(request)

    return {
            "model": model,
            "prediction": str(result),
            "name": species[result[0]]
            }