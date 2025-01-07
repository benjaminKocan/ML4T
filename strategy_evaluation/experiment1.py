import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import ManualStrategy
import marketsimcode as mktsim
from util import get_data
import StrategyLearner as sl
import datetime as dt



def test_in_sample():
    # Define parameters
    symbol = "JPM"
    start_date = "2008-01-01"
    end_date = "2009-12-31"
    start_val = 100000  # Starting value of the portfolio

    # Initialize ManualStrategy
    ms = ManualStrategy.ManualStrategy()

    # Test the Manual Strategy
    trades = ms.testPolicy(symbol, start_date, end_date, start_val)
    orders = []
    for date, row in trades.iterrows():
        if row[symbol] != 0:
            order_type = 'BUY' if row[symbol] > 0 else 'SELL'
            shares = abs(int(row[symbol]))
            orders.append([symbol, order_type, shares])

    orders_df = pd.DataFrame(orders, columns=['Symbol', 'Order', 'Shares'])
    orders_df.index = trades[trades[symbol] != 0].index  # Assigning the trade dates as index
    # Load price data for comparison
    prices = get_data([symbol], pd.date_range(start_date, end_date))[symbol]


    plt.title(f"Manual vs Learner vs Benchmark Portfolio Performance {symbol} In-Sample")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    # plt.plot(buy_trades.index, prices.loc[buy_trades.index], '^', color='green', markersize=10, label='Buy Signal')
    # plt.plot(sell_trades.index, prices.loc[sell_trades.index], 'v', color='red', markersize=10, label='Sell Signal')

    valid_start_date = prices.index[0]  # Assuming 'prices' contains only valid trading days

    # Create a single order DataFrame for the first valid trading day
    single_order = {
        'Symbol': ['JPM'],
        'Order': ['BUY'],
        'Shares': [1000]
    }

    single_order_df = pd.DataFrame(single_order, index=[valid_start_date])

    strategy_portval = mktsim.compute_portvals(start_date, end_date, orders_df, 100000, 9.95, 0.005)
    benchmark_portval = mktsim.compute_portvals(start_date, end_date, single_order_df, 100000, 9.95, 0.005)
    learner = sl.StrategyLearner(verbose=False, impact=0.0, commission=0.0)  # constructor
    learner.add_evidence(symbol=symbol, sd=start_date, ed=end_date,
                         sv=start_val)  # training phase
    df_trades = learner.testPolicy(symbol="JPM", sd=start_date, ed=end_date,
                                   sv=start_val)  # testing phase

    orders2 = []
    for date, row in df_trades.iterrows():
        if row[symbol] != 0:
            order_type = 'BUY' if row[symbol] > 0 else 'SELL'
            shares = abs(int(row[symbol]))
            orders2.append([symbol, order_type, shares])

    orders_df2 = pd.DataFrame(orders, columns=['Symbol', 'Order', 'Shares'])
    orders_df2.index = trades[trades[symbol] != 0].index  # Assigning the trade dates as index
    learner_portval = mktsim.compute_portvals(start_date, end_date, orders_df2, 100000, 9.95, 0.005)

    plt.plot(strategy_portval, color='red', label="Manual")
    plt.plot(benchmark_portval, color='purple', label="Benchmark")
    plt.plot(learner_portval, color='green', label="Learner")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.tight_layout()
    plt.plot()
    # plt.show()
    plt.savefig("./images/exp-1-in-sample.png")
    plt.clf()

def test_out_of_sample():
    # Define parameters
    symbol = "JPM"
    start_date = "2010-01-01"
    end_date = "2011-12-31"
    start_val = 100000  # Starting value of the portfolio

    # Initialize ManualStrategy
    ms = ManualStrategy.ManualStrategy()

    # Test the Manual Strategy
    trades = ms.testPolicy(symbol, start_date, end_date, start_val)
    orders = []
    for date, row in trades.iterrows():
        if row[symbol] != 0:
            order_type = 'BUY' if row[symbol] > 0 else 'SELL'
            shares = abs(int(row[symbol]))
            orders.append([symbol, order_type, shares])

    orders_df = pd.DataFrame(orders, columns=['Symbol', 'Order', 'Shares'])
    orders_df.index = trades[trades[symbol] != 0].index  # Assigning the trade dates as index
    # Load price data for comparison
    prices = get_data([symbol], pd.date_range(start_date, end_date))[symbol]

    # Load price data for comparison
    prices = get_data([symbol], pd.date_range(start_date, end_date))[symbol]


    plt.title(f"Manual vs Learner vs Benchmark Porfolio Performance for {symbol} Out-of-Sample")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    # plt.plot(buy_trades.index, prices.loc[buy_trades.index], '^', color='green', markersize=10, label='Buy Signal')
    # plt.plot(sell_trades.index, prices.loc[sell_trades.index], 'v', color='red', markersize=10, label='Sell Signal')

    valid_start_date = prices.index[0]  # Assuming 'prices' contains only valid trading days

    # Create a single order DataFrame for the first valid trading day
    single_order = {
        'Symbol': ['JPM'],
        'Order': ['BUY'],
        'Shares': [1000]
    }

    single_order_df = pd.DataFrame(single_order, index=[valid_start_date])

    strategy_portval = mktsim.compute_portvals(start_date, end_date, orders_df, 100000, 9.95, 0.005)

    benchmark_portval = mktsim.compute_portvals(start_date, end_date, single_order_df, 100000, 9.95, 0.005)

    learner = sl.StrategyLearner(verbose=False, impact=0.0, commission=0.0)  # constructor
    learner.add_evidence(symbol=symbol, sd="2008-01-01", ed="2009-12-31",
                         sv=start_val)  # training phase
    df_trades = learner.testPolicy(symbol="JPM", sd=start_date, ed=end_date,
                                   sv=start_val)  # testing phase

    orders2 = []
    for date, row in df_trades.iterrows():
        if row[symbol] != 0:
            order_type = 'BUY' if row[symbol] > 0 else 'SELL'
            shares = abs(int(row[symbol]))
            orders2.append([symbol, order_type, shares])

    orders_df2 = pd.DataFrame(orders, columns=['Symbol', 'Order', 'Shares'])
    orders_df2.index = trades[trades[symbol] != 0].index  # Assigning the trade dates as index
    # Load price data for comparison
    prices = get_data([symbol], pd.date_range(start_date, end_date))[symbol]


    learner_portval = mktsim.compute_portvals(start_date, end_date, orders_df2, 100000, 9.95, 0.005)


    plt.plot(strategy_portval, color='red', label='Manual')
    plt.plot(benchmark_portval, color='purple', label='Benchmark')
    plt.plot(learner_portval, color='green', label="Learner")
    plt.legend()
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.grid(True)
    plt.tight_layout()
    plt.plot()
    # plt.show()
    plt.savefig("./images/exp-1-out-of-sample.png")
    plt.clf()

    # Additional analysis (e.g., comparing to a benchmark, computing statistics) goes here
def run_experiment_1():
    # test_manual_strategy_in_sample()
    # test_manual_strategy_out_of_sample()
    test_in_sample()
    test_out_of_sample()


if __name__ == "__main__":
    run_experiment_1()



