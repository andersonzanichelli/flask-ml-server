from iris import Iris
from model_runner import ModelRunner
import logging

class Service:

    def __init__(self, model_filename):
        self.model = model_filename

    def create_iris(self, request):
        return Iris(request)

    def execute(self, request):
        iris = self.create_iris(request)

        logging.info(f'Created iris dto to send to model. Iris: {iris}')

        return ModelRunner(self.model).run(iris)