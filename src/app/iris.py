import numpy as np

class Iris:

    def __init__(self, request):
        self.sepal_length = float(request.args.get('sepal_length'))
        self.sepal_width = float(request.args.get('sepal_width'))
        self.petal_length = float(request.args.get('petal_length'))
        self.petal_width = float(request.args.get('petal_width'))

    def get_np_attr(self):
        return np.array([[
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width]])