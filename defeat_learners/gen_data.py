""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
template for generating data to fool learners (c) 2016 Tucker Balch  		  	   		  		 		  		  		    	 		 		   		 		  
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
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import math  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
# this function should return a dataset (X and Y) that will work  		  	   		  		 		  		  		    	 		 		   		 		  
# better for linear regression than decision trees  		  	   		  		 		  		  		    	 		 		   		 		  
def best_4_lin_reg(seed=1489683273):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		  		 		  		  		    	 		 		   		 		  
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		  		 		  		  		    	 		 		   		 		  
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param seed: The random seed for your data generation.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type seed: int  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: numpy.ndarray  		  	   		  		 		  		  		    	 		 		   		 		  
    """

    # np.random.seed(seed)
    # x = np.zeros((100, 2))
    # y = np.random.random(size=(100,)) * 200 - 100
    # Here's is an example of creating a Y from randomly generated
    # X with multiple columns
    # y = x[:,0] + np.sin(x[:,1]) + x[:,2]**2 + x[:,3]**3

    # generate data that can be described by a linear equation
    np.random.seed(seed)
    x = np.random.rand(100, 2)
    y = x[:, 0] * 25 + x[:, 1] * 15 + np.random.randn(100) * 10
    return x, y
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def best_4_dt(seed=1489683273):
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		  		 		  		  		    	 		 		   		 		  
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		  		 		  		  		    	 		 		   		 		  
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param seed: The random seed for your data generation.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type seed: int  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: numpy.ndarray  		  	   		  		 		  		  		    	 		 		   		 		  
    """
    # np.random.seed(seed)
    # x = np.random.rand(100, 2)  # Generate 100 data points with 10 features
    # # Complex, non-linear relationship
    # # y = (x[:, 0] ** 2 + np.exp(x[:, 1]))
    # y = np.sin(x[:, 0]) * np.cos(x[:, 1]) + np.random.randn(100) * 0.1
    # return x, y
    # np.random.seed(seed)
    # x = np.random.rand(100, 2)
    # y = (x[:, 0] ** 2 + np.sin(10 * x[:, 1]) + np.random.randn(100) * 0.1)
    # return x, y

    # perform non linear functions
    # not good enough if only 1 applied to each variable, needs more complexity
    np.random.seed(seed)
    x = np.random.rand(100, 2)
    y = (x[:, 0] ** 5 * np.sin(10 * x[:, 1]) + np.exp(x[:, 1]) * np.cos(5 * x[:, 0]) + np.log(1 + x[:, 0]) * np.sin(2 * np.pi * x[:, 1]) + np.random.randn(100) * 0.5)
    return x, y

  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return "bkocan3"  # Change this to your user ID
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    # print("they call me Tim.")
    pass
