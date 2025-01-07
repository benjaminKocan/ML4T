import numpy as np
import pandas as pd

class DTLearner(object):
    def __init__(self, leaf_size = 1, verbose=False):
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
        # first we need to bring data x and data y in as an array
        df = pd.DataFrame(data_x)
        df['Y'] = data_y
        self.tree = self.build_tree(df)


    def build_tree(self, data):

        if data.shape[0] <= self.leaf_size or len(pd.unique(data.iloc[:, -1])) == 1:
            return (np.array([-1, data.iloc[0, -1], np.nan, np.nan]).reshape(1, 4))

        else:
            # find the index of the most correlated feature
            # corr_df = data.corr()
            # corr_results = corr_df['Y'].drop('Y')
            # most_correlated = corr_results.idxmax()

            corr_coeffs = np.corrcoef(data.iloc[:, :-1], data.iloc[:, -1], rowvar=False)
            most_correlated = np.argmax(np.abs(corr_coeffs[:-1, -1]))

            # find median of the data in the MCI column
            split_val = np.median(data[most_correlated])
            # print("most corr ", most_correlated)
            # print("split_val out", split_val)


            # potential_splits = data[most_correlated] <= split_val
            # print("potential splits" + str(potential_splits))
            potential_splits = data.iloc[:, most_correlated] <= split_val
            # no good split val, quickly grab the min and move on
            if data[most_correlated].shape[0] <= data[potential_splits].shape[0]:
                # split_val = data[most_correlated].min()
                return (np.array([-1, data.iloc[0, -1], np.nan, np.nan]).reshape(1, 4))
                # print("split_val in", split_val)

            left_tree = self.build_tree(data[data.iloc[:, most_correlated] <= split_val])
            right_tree = self.build_tree(data[data.iloc[:, most_correlated] > split_val])
            root = [most_correlated, split_val, 1, len(left_tree)+1]
            return(np.vstack([root, left_tree, right_tree]))

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

        return Ypred
