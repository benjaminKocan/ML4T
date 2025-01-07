import numpy as np


class BagLearner(object):
    def __init__(self, learner, kwargs, bags, boost=False, verbose=False):
        """
        Constructor method
        """
        self.learner = learner
        self.kwargs = kwargs
        self.bags = bags
        self.boost = boost
        self.verbose = verbose
        self.learners = []
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        return "bkocan3"  # replace tb34 with your Georgia Tech username

    def add_evidence(self, data_x, data_y):
        all_points = data_x.shape[0]
        # print("all points", all_points)
        # print("size data x", data_x.shape[0])
        for i in range(self.bags):
            # print("we're running")
            # with replacement is key, means not all bags will be the same
            rands = np.random.choice(all_points, all_points, replace=True)
            # print("rands", rands)
            trainx = data_x[rands]
            trainy = data_y[rands]

            new_learner = self.learner(**self.kwargs)
            new_learner.add_evidence(trainx, trainy)
            self.learners.append(new_learner)

    def query(self, points):
        # for i in self.learners:
        #     # create an array containing query results -- mean?
        #     results = np.array([i.query(points)])
        # val = np.mean(results, axis=0)
        # return val
        predictions = np.zeros(points.shape[0])
        for learner in self.learners:
            predictions += learner.query(points)
        return predictions / len(self.learners)