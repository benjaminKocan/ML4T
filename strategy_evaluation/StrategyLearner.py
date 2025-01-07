""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
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
  		  	   		  		 		  		  		    	 		 		   		 		  
import datetime as dt
import random

import pandas as pd
import util as ut
import indicators as ind
from RTLearner import RTLearner
from BagLearner import BagLearner
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
class StrategyLearner(object):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  		 		  		  		    	 		 		   		 		  
        If verbose = False your code should not generate ANY output.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type verbose: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		  		 		  		  		    	 		 		   		 		  
    :type impact: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :param commission: The commission amount charged, defaults to 0.0  		  	   		  		 		  		  		    	 		 		   		 		  
    :type commission: float  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    # constructor  		  	   		  		 		  		  		    	 		 		   		 		  
    def __init__(self, verbose=False, impact=0.0, commission=0.0):
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        Constructor method  		  	   		  		 		  		  		    	 		 		   		 		  
        """
        self.learner = BagLearner(learner=RTLearner, kwargs={"leaf_size": 10}, bags=20, verbose=verbose)
        self.verbose = verbose
        self.impact = impact  		  	   		  		 		  		  		    	 		 		   		 		  
        self.commission = commission  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # this method should create a QLearner, and train it for trading
    def calculate_classifications(self, prices, N=20, YBUY=0.1, YSELL=-0.1):
        y_data = pd.Series(index=prices.index, data=0)  # default to 0 (CASH)

        for t in range(len(prices) - N):
            future_price = prices.iloc[t + N]
            current_price = prices.iloc[t]
            ret = (future_price / current_price) - 1.0
            # print(ret)

            if ret > YBUY:
                # print("long")
                y_data.iloc[t] = 1  # LONG
            elif ret < YSELL:
                # print("sell")
                y_data.iloc[t] = -1  # SHORT
        # print(y_data)
        return y_data

    def add_evidence(
        self,  		  	   		  		 		  		  		    	 		 		   		 		  
        symbol="IBM",  		  	   		  		 		  		  		    	 		 		   		 		  
        sd=dt.datetime(2008, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
        ed=dt.datetime(2009, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
        sv=10000,  		  	   		  		 		  		  		    	 		 		   		 		  
    ):  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        Trains your strategy learner over a given time frame.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
        :param symbol: The stock symbol to train on  		  	   		  		 		  		  		    	 		 		   		 		  
        :type symbol: str  		  	   		  		 		  		  		    	 		 		   		 		  
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  		 		  		  		    	 		 		   		 		  
        :type sd: datetime  		  	   		  		 		  		  		    	 		 		   		 		  
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  		 		  		  		    	 		 		   		 		  
        :type ed: datetime  		  	   		  		 		  		  		    	 		 		   		 		  
        :param sv: The starting value of the portfolio  		  	   		  		 		  		  		    	 		 		   		 		  
        :type sv: int  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
        # add your code to do learning here  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
        # example usage of the old backward compatible util function  		  	   		  		 		  		  		    	 		 		   		 		  
        syms = [symbol]  		  	   		  		 		  		  		    	 		 		   		 		  
        dates = pd.date_range(sd, ed)  		  	   		  		 		  		  		    	 		 		   		 		  
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY  		  	   		  		 		  		  		    	 		 		   		 		  
        prices = prices_all[syms]  # only portfolio symbols

        bbp = ind.calculate_bollinger_bands(symbol, sd, ed)
        rsi = ind.calculate_rsi(symbol, sd, ed)
        macd = ind.calculate_macd(symbol, sd, ed)

        # Combine indicators into a single DataFrame
        indicators = pd.DataFrame(index=prices.index)
        indicators['BBP'] = bbp
        indicators['RSI'] = rsi
        indicators['MACD'] = macd

        y_data = self.calculate_classifications(prices[symbol])
        # print(y_data)
        self.learner.add_evidence(indicators.values, y_data.values)

        prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		  		 		  		  		    	 		 		   		 		  
        if self.verbose:  		  	   		  		 		  		  		    	 		 		   		 		  
            print(prices)  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
        # example use with new colname  		  	   		  		 		  		  		    	 		 		   		 		  
        volume_all = ut.get_data(  		  	   		  		 		  		  		    	 		 		   		 		  
            syms, dates, colname="Volume"  		  	   		  		 		  		  		    	 		 		   		 		  
        )  # automatically adds SPY  		  	   		  		 		  		  		    	 		 		   		 		  
        volume = volume_all[syms]  # only portfolio symbols  		  	   		  		 		  		  		    	 		 		   		 		  
        volume_SPY = volume_all["SPY"]  # only SPY, for comparison later  		  	   		  		 		  		  		    	 		 		   		 		  
        if self.verbose:  		  	   		  		 		  		  		    	 		 		   		 		  
            print(volume)  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # this method should use the existing policy and test it against new data  		  	   		  		 		  		  		    	 		 		   		 		  
    def testPolicy(  		  	   		  		 		  		  		    	 		 		   		 		  
        self,  		  	   		  		 		  		  		    	 		 		   		 		  
        symbol="IBM",  		  	   		  		 		  		  		    	 		 		   		 		  
        sd=dt.datetime(2009, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
        ed=dt.datetime(2010, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
        sv=10000,  		  	   		  		 		  		  		    	 		 		   		 		  
    ):

        prices = ut.get_data([symbol], pd.date_range(sd, ed))[symbol]
        bbp = ind.calculate_bollinger_bands(symbol, sd, ed)
        rsi = ind.calculate_rsi(symbol, sd, ed)
        macd = ind.calculate_macd(symbol, sd, ed)

        # print(bbp)
        # print(rsi)
        # print(macd)

        # Combine indicators into a single DataFrame
        indicators = pd.DataFrame(index=prices.index)
        indicators['BBP'] = bbp
        indicators['RSI'] = rsi
        indicators['MACD'] = macd

        predictions = self.learner.query(indicators.values)
        trades = pd.DataFrame(data=0, index=prices.index, columns=[symbol])
        current_position = 0

        # Generate trades based on model predictions
        for i in range(len(predictions)):
            if predictions[i] == 1 and current_position != 1000:
                trades[symbol].iloc[i] = 1000 - current_position
                current_position = 1000
            elif predictions[i] == -1 and current_position != -1000:
                trades[symbol].iloc[i] = -1000 - current_position
                current_position = -1000

        orders = []
        for date, row in trades.iterrows():
            if row[symbol] != 0:
                order_type = 'BUY' if row[symbol] > 0 else 'SELL'
                shares = abs(int(row[symbol]))
                orders.append([symbol, order_type, shares])

        orders_df = pd.DataFrame(orders, columns=['Symbol', 'Order', 'Shares'])
        orders_df.index = trades[trades[symbol] != 0].index
        # print(orders_df)
        return trades
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    print("One does not simply think up a strategy")  		  	   		  		 		  		  		    	 		 		   		 		  
