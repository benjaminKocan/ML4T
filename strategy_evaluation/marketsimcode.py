""""""
"""MC2-P1: Market simulator.  		  	   		  		 		  		  		    	 		 		   		 		  

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
import os
import numpy as np
import pandas as pd
from util import get_data, plot_data
from matplotlib import pyplot as plt


def compute_portvals(
    start_date,
    end_date,
    trades_df,
    start_val=1000000,
    commission=9.95,
    impact=0.005,

):
    # Assuming trades_df is a DataFrame with columns ['Symbol', 'Order', 'Shares']
    # and the index is the datetime of the trades

    # Sort trades DataFrame just in case
    trades_df = trades_df.sort_index()

    # get unique symbols and dates
    symbols = list(set(trades_df['Symbol']))
    dates = trades_df.index.unique()
    start_date = start_date
    end_date = end_date

    prices_data = get_data(symbols, pd.date_range(start_date, end_date))

    # prices df
    df_prices = pd.DataFrame(prices_data)
    df_prices['cash'] = 1.0

    # trades df
    df_trades = df_prices.copy()
    # set everything to 0
    df_trades[:] = 0

    # populate trades df
    for index, row in trades_df.iterrows():
        symbol = row['Symbol']
        order_type = row['Order']
        shares = row['Shares']
        order_value = shares * df_prices.at[index, symbol]

        if order_type == 'BUY':
            impact_cost = impact * order_value
            df_trades.at[index, symbol] += shares
            df_trades.at[index, 'cash'] -= order_value + commission + impact_cost
        elif order_type == 'SELL':
            impact_cost = impact * order_value
            df_trades.at[index, symbol] -= shares
            df_trades.at[index, 'cash'] += order_value - commission - impact_cost

    # holdings df
    df_holdings = df_trades.copy()
    df_holdings[:] = 0

    # need to account for trades made on the first day
    df_holdings.loc[df_holdings.index[0], 'cash'] = start_val + df_trades.loc[df_trades.index[0], 'cash']
    df_holdings.iloc[0, :-1] = df_trades.iloc[0, :-1]

    # iterating through each day and adjusting holdings based on trades
    for day in range(1, len(df_holdings)):
        # previous days value plus whatever happened today
        df_holdings.iloc[day] = df_holdings.iloc[day - 1] + df_trades.iloc[day]

    # print(df_holdings)

    # values df
    df_values = df_holdings.copy()
    df_values[:] = 0

    # populate values df by multiplying holdings by current prices
    for symbol in symbols:
        df_values[symbol] = df_holdings[symbol] * df_prices[symbol]

    df_values['cash'] = df_holdings['cash']
    df_port_val = df_values.sum(axis=1)

    # port val df
    df_port_val = pd.DataFrame(df_port_val, columns=['Portfolio Value'])
    # print(df_port_val)

    return df_port_val


def author():
    return "bkocan3"  # replace tb34 with your Georgia Tech username.
