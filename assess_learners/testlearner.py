""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
Test a learner.  (c) 2015 Tucker Balch  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import math  		  	   		  		 		  		  		    	 		 		   		 		  
import sys  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
  		  	   		  		 		  		  		    	 		 		   		 		  
import LinRegLearner as lrl
import DTLearner as dt
import RTLearner as rt
import InsaneLearner as it
import BagLearner as bl
  		  	   		  		 		  		  		    	 		 		   		 		  
def show_fig_1(train_x, train_y, test_x, test_y):
    in_sample_rmse = []
    out_of_sample_rmse = []
    leaf_sizes = range(1, 51)
    for i in leaf_sizes:
        learner = dt.DTLearner(leaf_size=i, verbose=True)
        # learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": i}, bags=20, boost=False, verbose=False)
        learner.add_evidence(train_x, train_y)

        # evaluate in sample
        pred_y = learner.query(train_x)  # get the predictions
        in_rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
        in_sample_rmse.append(in_rmse)

        # evaluate out of sample
        pred_y = learner.query(test_x)  # get the predictions
        out_rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
        out_of_sample_rmse.append(out_rmse)

    plt.plot(leaf_sizes, in_sample_rmse, label='In sample')
    plt.plot(leaf_sizes, out_of_sample_rmse, label='Out of sample')
    plt.xlabel('Leaf Size')
    plt.ylabel('RMSE Value')
    plt.title('Figure 1: RMSE Value as Leaf Size Increases')
    plt.axvline(x=4, color='gray', linestyle='--', label='Overfitting')
    plt.legend()
    #
    plt.show()

def show_fig_2(train_x, train_y, test_x, test_y):
    in_sample_rmse = []
    out_of_sample_rmse = []
    leaf_sizes = range(1, 51)
    for i in leaf_sizes:
        learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": i}, bags=20, boost=False, verbose=False)
        learner.add_evidence(train_x, train_y)

        # evaluate in sample
        pred_y = learner.query(train_x)  # get the predictions
        in_rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
        in_sample_rmse.append(in_rmse)

        # evaluate out of sample
        pred_y = learner.query(test_x)  # get the predictions
        out_rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
        out_of_sample_rmse.append(out_rmse)

    plt.plot(leaf_sizes, in_sample_rmse, label='In sample')
    plt.plot(leaf_sizes, out_of_sample_rmse, label='Out of sample')
    plt.xlabel('Leaf Size')
    plt.ylabel('RMSE Value')
    plt.title('Figure 2: Does Bagging Help Overfitting?')
    plt.axvline(x=6, color='gray', linestyle='--', label='Overfitting')

    plt.legend()
    #
    plt.show()

def compare_max_error(train_x, train_y, test_x, test_y):
    rt_abs_error = []
    dt_abs_error = []
    rt_max_error = []
    dt_max_error = []
    leaf_sizes = range(1, 51)
    for i in leaf_sizes:
        rt_learner = rt.RTLearner(leaf_size=i, verbose=True)
        dt_learner = dt.DTLearner(leaf_size=i, verbose=True)
        rt_learner.add_evidence(train_x, train_y)
        dt_learner.add_evidence(train_x, train_y)
        rt_pred = rt_learner.query(test_x)
        dt_pred = dt_learner.query(test_x)

        rt_abs_error.append(np.abs(rt_pred - test_y))
        dt_abs_error.append(np.abs(dt_pred - test_y))

        rt_max_error.append(np.max(rt_abs_error))
        dt_max_error.append(np.max(dt_abs_error))

        # print("rt Max error", rt_max_error)
        # print("rt Max error length", rt_max_error.shape[0])
        # print("dt Max error", dt_max_error)

    plt.plot(leaf_sizes, rt_max_error, label='RTLearner Max Error')
    plt.plot(leaf_sizes, dt_max_error, label='DTLearner Max Error')
    plt.xlabel('Leaf Size')
    plt.ylabel('Abs Error')
    plt.title('Figure 3: How Leaf Size Affects Absolute Error')
    plt.legend()
    #
    plt.show()


def calculate_r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    return r_squared


def compare_r_squared(train_x, train_y, test_x, test_y):
    rt_r_squared = []
    dt_r_squared = []
    leaf_sizes = range(1, 51)

    for i in leaf_sizes:
        rt_learner = rt.RTLearner(leaf_size=i, verbose=True)
        dt_learner = dt.DTLearner(leaf_size=i, verbose=True)
        rt_learner.add_evidence(train_x, train_y)
        dt_learner.add_evidence(train_x, train_y)
        rt_pred = rt_learner.query(test_x)
        dt_pred = dt_learner.query(test_x)

        # Calculate R-Squared using the custom function
        rt_r_squared.append(calculate_r_squared(test_y, rt_pred))
        dt_r_squared.append(calculate_r_squared(test_y, dt_pred))

    # plt.plot(leaf_sizes, rt_r_squared, label='RTLearner R-Squared')
    # plt.plot(leaf_sizes, dt_r_squared, label='DTLearner R-Squared')
    # plt.xlabel('Leaf Size')
    # plt.ylabel('R-Squared')
    # plt.title('How Leaf Size Affects R-Squared')
    # plt.legend()
    # plt.show()

    print(rt_r_squared)
    print(dt_r_squared)


if __name__ == "__main__":
    if len(sys.argv) != 2:  		  	   		  		 		  		  		    	 		 		   		 		  
        print("Usage: python testlearner.py <filename>")  		  	   		  		 		  		  		    	 		 		   		 		  
        sys.exit(1)  		  	   		  		 		  		  		    	 		 		   		 		  
    inf = open(sys.argv[1])  		  	   		  		 		  		  		    	 		 		   		 		  
    data = np.array(
        [list(map(float, s.strip().split(",")[1:])) for s in inf.readlines()[1:]]
    )

    # data = np.array(
    #     [list(map(float, s.strip().split(","))) for s in inf.readlines()]
    # )


    # data_input = [[.885, .330, 9.1, 4.0],
    #     [.725, .390, 10.9, 5.0],
    #     [.560, .5, 9.4, 6.0],
    #     [.735, .57, 9.8, 5.0],
    #     [.610, .630, 8.4, 3.0],
    #     [.26, .63, 10.5, 7.0],
    #     [.5, .68, 10.5, 7.0],
    #     [.32, .78, 10.0, 6.0]]

    # data_test = pd.DataFrame(data_input, columns=["x2", "x10", "x11", "y"])
    #
    # # print(data_test)
    #
    #
    # # compute how much of the data is training and testing
    train_rows = int(0.6 * data.shape[0])
    test_rows = data.shape[0] - train_rows
    # #
    # separate out training and testing data
    train_x = data[:train_rows, 0:-1]
    train_y = data[:train_rows, -1]
    test_x = data[train_rows:, 0:-1]
    test_y = data[train_rows:, -1]
    #
    # testing_x = [[.885, .330, 9.1],
    #     [.725, .390, 10.9],
    #     [.560, .5, 9.4],
    #     [.735, .57, 9.8],
    #     [.610, .630, 8.4],
    #     [.26, .63, 10.5],
    #     [.5, .68, 10.5],
    #     [.32, .78, 10.0]]
    #
    # testing_y = [[4.0],
    #     [5.0],
    #     [6.0],
    #     [5.0],
    #     [3.0],
    #     [7.0],
    #     [7.0],
    #     [ 6.0]]
    #
    # data_new = [x + y for x, y in zip(testing_x, testing_y)]
    #
    # # Create DataFrame
    # columns = ["x2", "x10", "x11", "y"]
    # testing_data_new = pd.DataFrame(data_new, columns=columns)
    #
    # # print(testing_data_new)
    #
    # x_values = testing_data_new.iloc[:, :-1].values
    # y_values = testing_data_new.iloc[:, -1].values


    # print(x_values)
    # print(y_values)

    learner = dt.DTLearner(leaf_size=1, verbose=True)
    learner.add_evidence(train_x, train_y)
    # print(data)
    # print(learner.tree)

    # data_new = [x + y for x, y in zip(testing_x, testing_y)]

    # Create DataFrame
    # columns = ["x2", "x10", "x11", "y"]
    # testing_data_new = pd.DataFrame(data_new, columns=columns)
    #
    # print(testing_data_new)

    # print(f"{test_x.shape}")
    # print(f"{test_y.shape}")
    show_fig_1(train_x, train_y, test_x, test_y)
    # show_fig_2(train_x, train_y, test_x, test_y)
    compare_max_error(train_x, train_y, test_x, test_y)
    # compare_r_squared(train_x, train_y, test_x, test_y)
    # learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": 1}, bags=20, boost=False, verbose=False)


    # create a learner and train it
    # learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": 1}, bags=20, boost=False, verbose=False)
    # learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner
    # learner = rt.RTLearner(leaf_size=1, verbose=True)

    # # train it
    # # # evaluate in sample
    pred_y = learner.query(train_x)  # get the predictions
    rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    #
    print()
    print("In sample results")
    print(f"RMSE: {rmse}")
    c = np.corrcoef(pred_y, y=train_y)
    print(f"corr: {c[0,1]}")

    # evaluate out of sample
    pred_y = learner.query(test_x)  # get the predictions
    rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    print()
    print("Out of sample results")
    print(f"RMSE: {rmse}")
    c = np.corrcoef(pred_y, y=test_y)
    print(f"corr: {c[0,1]}")



