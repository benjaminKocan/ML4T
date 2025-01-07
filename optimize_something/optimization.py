""""""
"""MC1-P2: Optimize a portfolio.  		  	   		  		 			  		 			 	 	 		 		 	

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

Student Name: Benjamin Kocan (replace with your name)  		  	   		  		 			  		 			 	 	 		 		 	
GT User ID: bkocan3 (replace with your User ID)  		  	   		  		 			  		 			 	 	 		 		 	
GT ID: 903952660 (replace with your GT ID)  		  	   		  		 			  		 			 	 	 		 		 	
"""

import datetime as dt

import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from util import get_data, plot_data
import scipy.optimize as spo
# from pandas.plotting import register_matplotlib_converters

def author():
    """
    :return: The GT username of the student
    :rtype: str
    """
    return "bkocan3"  # replace tb34 with your Georgia Tech username.


def gtid():
    """
    :return: The GT ID of the student
    :rtype: int
    """
    return 903952660  # replace with your GT ID number

# This is the function that will be tested by the autograder
# The student must update this code to properly implement the functionality
def optimize_portfolio(
        sd=dt.datetime(2008, 1, 1),
        ed=dt.datetime(2009, 1, 1),
        syms=["GOOG", "AAPL", "GLD", "XOM"],
        gen_plot=False,
):
    """
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and
    statistics.

    :param sd: A datetime object that represents the start date, defaults to 1/1/2008
    :type sd: datetime
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009
    :type ed: datetime
    :param syms: A list of symbols that make up the portfolio (note that your code should support any
        symbol in the data directory)
    :type syms: list
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your
        code with gen_plot = False.
    :type gen_plot: bool
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,
        standard deviation of daily returns, and Sharpe ratio
    :rtype: tuple
    """

    # Read in adjusted closing prices for given symbols, date range
    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later

    # find the allocations for the optimal portfolio
    # note that the values here ARE NOT meant to be correct for a test case
    allocs = np.asarray(
        [0.2, 0.2, 0.3, 0.3]
    )  # add code here to find the allocations
    cr, adr, sddr, sr = [
        0.25,
        0.001,
        0.0005,
        2.1,
    ]  # add code here to compute stats

    size = len(syms)
    guess = [1.0/size] * size
    bounds = [(0.0, 1.0)] * size

    constraints = ({'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs)})

    allocs = spo.minimize(find_sharpe_ratio, guess, args=(prices,), method="SLSQP", bounds=bounds, constraints=constraints, options={'disp':True}).x
    print(allocs)
    cr, adr, sddr, sr, port_val = assess_portfolio(allocs, prices)
    # print(port_val)
    # print("allocs" + str(allocs))
    # Get daily portfolio value
    # port_val = prices_SPY  # add code here to compute daily portfolio values

    # Compare daily portfolio value with SPY using a normalized plot
    if gen_plot:
        # add code to plot here
        port_val = port_val / port_val[0]
        prices_SPY = prices_SPY / prices_SPY[0]
        df_temp = pd.concat(
            [port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1
        )
        # df_temp.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        #         fontsize=40, color='gray', alpha=0.5,
        #         ha='center', va='center', rotation=30)
        # plot_data(df_temp, title="Daily Portfolio Value and SPY", xlabel="Date", ylabel="Price")

        plt.plot(df_temp)
        plt.title("Daily Portfolio Value vs. SPY")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend(["Portfolio", "SPY"], loc="lower right")
        plt.savefig("./images/Figure1.png")
        # plt.show()
        pass

    return allocs, cr, adr, sddr, sr

def find_sharpe_ratio(allocs, prices):
    return -assess_portfolio(allocs, prices)[3]
def assess_portfolio(allocs, prices
        # sd=dt.datetime(2008, 1, 1),
        # ed=dt.datetime(2009, 1, 1),
        # syms=["GOOG", "AAPL", "GLD", "XOM"],
        # allocs=[0.1, 0.2, 0.3, 0.4],
        # sv=1000000,
        # rfr=0.0,
        # sf=252.0,
        # gen_plot=False,
):

    # # Read in adjusted closing prices for given symbols, date range
    # dates = pd.date_range(sd, ed)
    # prices_all = get_data(syms, dates)  # automatically adds SPY
    # prices = prices_all[syms]  # only portfolio symbols
    # prices_SPY = prices_all["SPY"]  # only SPY, for comparison later
    #
    # # Get daily portfolio value
    # port_val = prices_SPY  # add code here to compute daily portfolio values
    #
    # # Get portfolio statistics (note: std_daily_ret = volatility)
    # cr, adr, sddr, sr = [
    #     0.25,
    #     0.001,
    #     0.0005,
    #     2.1,
    # ]  # add code here to compute stats
    # # Read in adjusted closing prices for the equities.
    # # Normalize the prices according to the first day. The first row for each stock should have a value of 1.0 at this point.
    # # Multiply each column by the allocation to the corresponding equity.
    # # Multiply these normalized allocations by starting value of overall portfolio, to get position values.
    # # Sum each row (i.e. all position values for each day). That is your daily portfolio value.
    # # Compute statistics from the total portfolio value.

    normed = prices / prices.values[0]
    alloced = normed * allocs
    # position_values = alloced * sv <-- dont need when normalized
    port_val = alloced.sum(axis=1)

    copied = port_val.copy()
    cr = (copied[-1] / copied[0]) - 1
    adr_copied = port_val.copy()
    adr_copied[1:] = (adr_copied[1:] / adr_copied[:-1].values) - 1
    adr_copied[0] = 0
    adr = adr_copied.mean()
    sddr = adr_copied.std()
    sqrt_252 = 252 ** .5
    sr = sqrt_252 * (adr / sddr)

    # Compare daily portfolio value with SPY using a normalized plot

        # Add code here to properly compute end value
    ev = port_val[-1]

    return cr, adr, sddr, sr, port_val

def test_code():
    """
    This function WILL NOT be called by the auto grader.
    """

    start_date = dt.datetime(2008, 6, 1)
    end_date = dt.datetime(2009, 6, 1)
    # symbols = ["IBM", "X", "GLD", "JPM"]
    symbols = ["IBM", "X", "GLD", "JPM"]

    # Assess the portfolio
    allocations, cr, adr, sddr, sr = optimize_portfolio(
        sd=start_date, ed=end_date, syms=symbols, gen_plot=False
    )

    # Print statistics
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Symbols: {symbols}")
    print(f"Allocations:{allocations}")
    print(f"Sharpe Ratio: {sr}")
    print(f"Volatility (stdev of daily returns): {sddr}")
    print(f"Average Daily Return: {adr}")
    print(f"Cumulative Return: {cr}")


if __name__ == "__main__":
    # This code WILL NOT be called by the auto grader
    # Do not assume that it will be called
    test_code()