import numpy as np
import BagLearner as bl
import LinRegLearner as lrl
class InsaneLearner(object):
    def __init__(self, verbose=False):
        self.learners = []
        for i in range(20):
            learner = bl.BagLearner(learner=lrl.LinRegLearner, kwargs={}, bags=20, boost=False, verbose = False)
            self.learners.append(learner)
        self.verbose = verbose
    def author(self):
        return "bkocan3"  # replace tb34 with your Georgia Tech username
    def add_evidence(self, data_x, data_y):
        for i in self.learners:
            i.add_evidence(data_x, data_y)
    def query(self, points):
        return self.learners[0].query(points)