import numpy as np

class LogisticRegressionExplainability:
    def __init__(self, model):
        self.model = model

    def feature_importance(self):
        # Normalize weights to sum up to 1 for relative importance
        importance = self.model.weights / np.sum(np.abs(self.model.weights))
        return importance
