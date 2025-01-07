
"""For both sections:

Use only the data provided for this course. You are not allowed to import external data.
Add an author() function to each file.
For your report, use only the symbol JPM.
Use the time period January 1, 2008, to December 31, 2009.
Starting cash is $100,000.
Theoretically Optimal Strategy only:

Allowable positions are 1000 shares long, 1000 shares short, 0 shares. (You may trade up to 2000 shares at a time as long as your positions are 1000 shares long or 1000 shares short.)
Benchmark: The performance of a portfolio starting with $100,000 cash, investing in 1000 shares of JPM, and holding that position.
Transaction costs for TheoreticallyOptimalStrategy:
Commission: $0.00
Impact: 0.00.

testPolicy(symbol=”AAPL”, sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000)

"""
import datetime as dt
import os
import numpy as np
import pandas as pd
from util import get_data, plot_data
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import indicators


def __init__(self):
    """
    Constructor method
    """
    pass  # move along, these aren't the drones you're looking for

def author(self):
    return "bkocan3"  # replace tb34 with your Georgia Tech username

# get the benchmark of holding 1000 JPM between 1-1-2008 and 12-31-2009
def compute_benchmark(symbol="JPM", start_date="2008-01-01", end_date="2009-12-31", start_val=100000):
    dates = pd.date_range(start_date, end_date)
    prices = get_data([symbol], dates)[symbol]

    trades = pd.DataFrame(index=prices.index, columns=['Date', 'Symbol', 'Order', 'Shares'])
    trades['Date'] = prices.index
    trades['Symbol'] = symbol
    trades['Order'] = 'BUY'
    trades['Shares'] = 0
    trades.iloc[0, 3] = 1000  # Buy 1000 shares on the first day

    return trades

def compute_portvals(
    trades_df,
    start_val=1000000,
    commission=9.95,
    impact=0.005
):
    # Sort trades by date
    trades_df.sort_index(inplace=True)

    # get unique symbols and dates and sort on dates
    symbols = list(set(trades_df['Symbol']))
    dates = list(set(trades_df.index))
    dates.sort()

    start_date = dates[0]
    end_date = dates[-1]

    prices_data = get_data(symbols, pd.date_range(start_date, end_date))
    df_prices = pd.DataFrame(prices_data)
    df_prices['cash'] = 1.0

    # trades df
    df_trades = df_prices.copy()
    df_trades[:] = 0

    trades_df = trades_df[trades_df.index.isin(df_prices.index)]

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

    df_holdings.loc[df_holdings.index[0], 'cash'] = start_val + df_trades.loc[df_trades.index[0], 'cash']
    df_holdings.iloc[0, :-1] = df_trades.iloc[0, :-1]

    for day in range(1, len(df_holdings)):
        df_holdings.iloc[day] = df_holdings.iloc[day - 1] + df_trades.iloc[day]

    # values df
    df_values = df_holdings.copy()
    df_values[:] = 0

    for symbol in symbols:
        df_values[symbol] = df_holdings[symbol] * df_prices[symbol]

    df_values['cash'] = df_holdings['cash']
    df_port_val = df_values.sum(axis=1)

    df_port_val = pd.DataFrame(df_port_val, columns=['Portfolio Value'])

    return df_port_val
def display_table(benchmark_calcs, tos_calcs):
    # Header
    header = "{:<20} {:>20} {:>20} {:>20}".format(
        "Metric", "Benchmark", "TOS", "Difference"
    )
    print(header)
    print('-' * 80)  # Line separator

    # Metrics
    metrics = ["Cumulative Returns", "Std Dev Daily Returns", "Mean Daily Returns"]
    for i, metric in enumerate(metrics):
        print("{:<20} {:>20.6f} {:>20.6f} {:>20.6f}".format(
            metric, benchmark_calcs[i], tos_calcs[i], tos_calcs[i]-benchmark_calcs[i]
        ))
def calculate_metrics(port_val):
    daily_returns = port_val.pct_change().dropna()
    CR = (port_val.iloc[-1, 0] / port_val.iloc[0, 0]) - 1
    SDR = daily_returns.iloc[:, 0].std()
    MDR = daily_returns.iloc[:, 0].mean()
    # print(f"Cumulative Returns (CR): {CR:.6f}")
    # print(f"Standard Deviation of Daily Returns (SDR): {SDR:.6f}")
    # print(f"Mean Daily Returns (MDR): {MDR:.6f}")

    return CR, SDR, MDR
def testPolicy(symbol="JPM", sd="2008-01-01", ed="2009-12-31", sv=100000):
    dates = pd.date_range(sd, ed)
    prices = get_data([symbol], dates)[symbol]

    trades = pd.DataFrame(index=dates, columns=['Date', 'Symbol', 'Order', 'Shares'])
    trades['Date'] = dates
    trades['Symbol'] = symbol
    trades['Shares'] = 0

    # track if we are +/- 1000 or neutral
    position = 0

    # calculate future price movement
    # print(prices)
    future_movement = prices.shift(-1) - prices
    # print(future_movement)

    # if price is going to go up tomorrow, we should buy, vice versa
    for date, next_day_movement in future_movement[:-1].iteritems():
        # price is about to go up
        if next_day_movement > 0 and position != 1000:
            trades.loc[date, 'Order'] = 'BUY'
            trades.loc[date, 'Shares'] = 1000 - position
            position = 1000
        #     price is about to go down
        elif next_day_movement < 0 and position != -1000:
            trades.loc[date, 'Order'] = 'SELL'
            trades.loc[date, 'Shares'] = 1000 + position
            position = -1000

    theoretical_best_port_val = compute_portvals(trades, sv, 0.0, 0.0)
    benchmark_trades = compute_benchmark()
    benchmark_port_val = compute_portvals(benchmark_trades, 100000.00, 0.0, 0.0)

    benchmark_calcs = calculate_metrics(benchmark_port_val)
    tos_calcs = calculate_metrics(theoretical_best_port_val)

    # Normalize data
    theoretical_best_port_val /= theoretical_best_port_val.iloc[0]
    benchmark_port_val /= benchmark_port_val.iloc[0]

    # print(benchmark_calcs)
    # print(tos_calcs)
    # Plotting using matplotlib
    plt.figure(figsize=(12, 6))
    plt.plot(theoretical_best_port_val, color='red', label="Theoretical Best")
    plt.plot(benchmark_port_val, color='purple', label="Benchmark")
    plt.title("Theoretical Best vs Benchmark")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("./images/tos.png")
    plt.clf()


if __name__ == "__main__":
    testPolicy()



