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


def compute_portvals(
        orders_file="./orders/orders.csv",
        start_val=1000000,
        commission=9.95,
        impact=0.005,
):
    # orders_df = pd.read_csv(orders_file, index_col='Date', parse_dates=True)
    orders_df = pd.read_csv(orders_file, index_col='Date', parse_dates=True, na_values=['nan'])
    orders_df.sort_index(inplace=True)

    # get unique symbols and dates and sort on dates
    symbols = list(set(orders_df['Symbol']))
    dates = list(set(orders_df.index))
    dates.sort()

    start_date = dates[0]
    end_date = dates[-1]

    prices_data = get_data(symbols, pd.date_range(start_date, end_date))

    # prices df
    df_prices = pd.DataFrame(prices_data)
    df_prices['cash'] = 1.0

    # trades df
    df_trades = df_prices.copy()
    # set everything to 0
    df_trades[:] = 0

    # populate trades df
    for index, row in orders_df.iterrows():
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

    return df_port_val


def author():
    return "bkocan3"  # replace tb34 with your Georgia Tech username.


def test_code():

    of = "./orders/orders-01.csv"
    sv = 1000000

    # Process orders
    portvals = compute_portvals(orders_file=of, start_val=sv, commission=0, impact=0)
    if isinstance(portvals, pd.DataFrame):
        portvals = portvals[
            portvals.columns[0]]  # just get the first column
    else:
        "warning, code did not return a DataFrame"

    # CR
    initial_value = portvals.iloc[0]
    final_value = portvals.iloc[-1]
    cum_ret = (final_value / initial_value) - 1

    # Get portfolio stats
    df_daily_returns = portvals.pct_change()

    # ADR
    avg_daily_ret = df_daily_returns.mean()

    # STD Daily Return
    std_daily_ret = df_daily_returns.std()

    # Sharpe Ratio
    sharpe_ratio = (avg_daily_ret / std_daily_ret) * np.sqrt(252)

    # Get corresponding data for SPY
    start_date = portvals.index[0]
    end_date = portvals.index[-1]
    spy_data = get_data(['SPY'], pd.date_range(start_date, end_date))['SPY']

    # CR
    initial_value_SPY = spy_data.iloc[0]
    final_value_SPY = spy_data.iloc[-1]
    cum_ret_SPY = (final_value_SPY / initial_value_SPY) - 1

    df_spy_returns = spy_data.pct_change()

    # ADR
    avg_daily_ret_SPY = df_spy_returns.mean()

    # Standard Deviation of Daily Return
    std_daily_ret_SPY = df_spy_returns.std()

    # Sharpe Ratio
    sharpe_ratio_SPY = (avg_daily_ret_SPY / std_daily_ret_SPY) * np.sqrt(252)

    # Compare portfolio against $SPX
    # print(f"Date Range: {start_date} to {end_date}")
    # print()
    # print(f"Sharpe Ratio of Fund: {sharpe_ratio}")
    # print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")
    # print()
    # print(f"Cumulative Return of Fund: {cum_ret}")
    # print(f"Cumulative Return of SPY : {cum_ret_SPY}")
    # print()
    # print(f"Standard Deviation of Fund: {std_daily_ret}")
    # print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")
    # print()
    # print(f"Average Daily Return of Fund: {avg_daily_ret}")
    # print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")
    # print()
    # print(f"Final Portfolio Value: {portvals[-1]}")


if __name__ == "__main__":
    test_code()
