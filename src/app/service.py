from iris import Iris
from model_runner import ModelRunner

class Service:

    def __init__(self, model_filename):
        self.model = model_filename

    def create_iris(self, request):
        return Iris(request)

    def execute(self, request):
        iris = self.create_iris(request)
        return ModelRunner(self.model).run(iris)