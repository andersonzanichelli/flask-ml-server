import pickle
import logging

class ModelRunner:

    def __init__(self, model_name):
        self.model_name = model_name

    def load_model(self):
        logging.info(f'Loading the model {self.model_name}')
        with open(self.model_name, 'rb') as file:
            return pickle.load(file)

    def run(self, iris):
        model = self.load_model()
        logging.info(f'Running the model {self.model_name}')

        predicted = model.predict(iris.get_np_attr())

        logging.info(f'Value predicted by the model: {predicted}')

        return predicted
