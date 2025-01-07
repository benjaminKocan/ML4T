import numpy as np
import pandas as pd
from scipy.stats import mode

class RTLearner(object):
    def __init__(self, leaf_size=1, verbose=False):
        """
        Constructor method
        """
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.tree = None
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        return "bkocan3"  # replace tb34 with your Georgia Tech username

    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """
        np.random.seed(1481090000)
        df = pd.DataFrame(data_x)
        df['Y'] = data_y
        self.tree = self.build_tree(df)

        # slap on 1s column so linear regression finds a constant term
        # new_data_x = np.ones([data_x.shape[0], data_x.shape[1] + 1])
        # new_data_x[:, 0: data_x.shape[1]] = data_x
        #
        # # build and save the model
        # self.model_coefs, residuals, rank, s = np.linalg.lstsq(
        #     new_data_x, data_y, rcond=None
        # )

    def query(self, points):

        Ypred = np.empty(points.shape[0])

        for i in range(points.shape[0]):
            node = 0
            while self.tree[node, 0] != -1:  # This checks if it's a leaf node
                feature_index = int(self.tree[node, 0])
                split_val = self.tree[node, 1]
                if points[i, feature_index] <= split_val:
                    node = int(node + self.tree[node, 2])
                else:
                    node = int(node + self.tree[node, 3])
            Ypred[i] = self.tree[node, 1]  # Changed from self.tree[node, 3] to self.tree[node, 1]
        # print(Ypred)
        return Ypred

    def build_tree(self, data):
        np.random.seed(1481090000)
        # Check if data is empty
        if data.shape[0] == 0:
            # Return a leaf node with a default value, e.g., 0
            return np.array([[-1, 0, np.nan, np.nan]]).reshape(1, 4)

        if data.shape[0] <= self.leaf_size or len(pd.unique(data.iloc[:, -1])) == 1:
            # Calculate the mode of the target values
            most_common = mode(data['Y'])[0][0]
            most_common = np.clip(most_common, -1, 1)
            return np.array([-1, most_common, np.nan, np.nan]).reshape(1, 4)
        else:
            rand_feature = np.random.choice(data.columns[:-1])
            split_val = np.nanmedian(data.iloc[:, rand_feature])

            # Check if all split values are the same
            if data[rand_feature].shape[0] <= data[data.iloc[:, rand_feature] <= split_val].shape[0]:
                most_common = mode(data['Y'])[0][0]
                most_common = np.clip(most_common, -1, 1)
                return np.array([-1, most_common, np.nan, np.nan]).reshape(1, 4)

            left_tree = self.build_tree(data[data.iloc[:, rand_feature] <= split_val])
            right_tree = self.build_tree(data[data.iloc[:, rand_feature] > split_val])
            root = [rand_feature, split_val, 1, len(left_tree) + 1]
            return np.vstack([root, left_tree, right_tree])