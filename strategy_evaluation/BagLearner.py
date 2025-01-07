import numpy as np
from scipy.stats import mode


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
        np.random.seed(1481090000)
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
        predictions = [learner.query(points) for learner in self.learners]

        # Convert list of predictions to a numpy array
        predictions = np.array(predictions)

        # Use mode to decide the final output
        final_predictions = mode(predictions, axis=0)[0]

        return final_predictions.ravel()