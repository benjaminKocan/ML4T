import pandas as pd
import matplotlib.pyplot as plt
import ManualStrategy
import marketsimcode as mktsim
from util import get_data
import StrategyLearner as sl
import datetime as dt
import experiment1 as exp1
import experiment2 as exp2

def test_manual_strategy_in_sample():
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


    # Highlight buy and sell points
    buy_trades = orders_df[orders_df['Order'] == 'BUY']
    sell_trades = orders_df[orders_df['Order'] == 'SELL']
    plt.figure(figsize=(10, 6))
    for date in buy_trades.index:
        plt.axvline(x=date, color='blue', linestyle='--', label='Buy Signal' if date == buy_trades.index[0] else "")
    for date in sell_trades.index:
        plt.axvline(x=date, color='black', linestyle='--', label='Sell Signal' if date == sell_trades.index[0] else "")

    # Ensure that the legend only shows one entry per label
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())


    plt.title(f"Manual Trading Strategy for {symbol} In-Sample")
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


    plt.plot(strategy_portval, color='red', label="Manual Strategy")
    plt.plot(benchmark_portval, color='purple', label="Benchmark")
    plt.legend()
    plt.tight_layout()
    plt.savefig("./images/manual-strategy-in-sample.png")
    plt.clf()

    CR_strategy = (strategy_portval.iloc[-1] / strategy_portval.iloc[0]) - 1
    CR_benchmark = (benchmark_portval.iloc[-1] / benchmark_portval.iloc[0]) - 1

    strategy_daily_returns = strategy_portval.pct_change()
    benchmark_daily_returns = benchmark_portval.pct_change()

    strategy_adr = strategy_daily_returns.mean()
    benchmark_adr = benchmark_daily_returns.mean()

    strategy_std_dev_daily_returns = strategy_daily_returns.std()
    benchmark_std_dev_daily_returns = benchmark_daily_returns.std()

    # print("CR Strategy:", float(CR_strategy))
    # print("CR Benchmark:", float(CR_benchmark))
    #
    # print("STD Daily Returns Strategy", float(strategy_std_dev_daily_returns))
    # print("STD Daily Returns Benchmark", float(benchmark_std_dev_daily_returns))
    #
    # print("Mean Daily Returns Strategy", float(strategy_adr))
    # print("Mean Daily Returns Benchmark", float(benchmark_adr))
    # plt.show()

    # Additional analysis (e.g., comparing to a benchmark, computing statistics) goes here
def test_manual_strategy_out_of_sample():
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


    # Highlight buy and sell points
    buy_trades = orders_df[orders_df['Order'] == 'BUY']
    sell_trades = orders_df[orders_df['Order'] == 'SELL']
    plt.figure(figsize=(10, 6))
    for date in buy_trades.index:
        plt.axvline(x=date, color='blue', linestyle='--', label='Buy Signal' if date == buy_trades.index[0] else "")
    for date in sell_trades.index:
        plt.axvline(x=date, color='black', linestyle='--', label='Sell Signal' if date == sell_trades.index[0] else "")

    # Ensure that the legend only shows one entry per label
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())


    plt.title(f"Manual Strategy for {symbol} Out-of-Sample")
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

    strategy_portval = mktsim.compute_portvals(start_date, end_date, orders_df,100000, 9.95, 0.005)
    benchmark_portval = mktsim.compute_portvals(start_date, end_date, single_order_df,100000, 9.95, 0.005)
    plt.plot(strategy_portval, color='red', label="Manual Strategy")
    plt.plot(benchmark_portval, color='purple', label="Benchmark")
    plt.legend()
    plt.tight_layout()
    # plt.show()
    plt.savefig("./images/manual-strategy-out-of-sample.png")
    plt.clf()

    CR_strategy = (strategy_portval.iloc[-1] / strategy_portval.iloc[0]) - 1
    CR_benchmark = (benchmark_portval.iloc[-1] / benchmark_portval.iloc[0]) - 1

    strategy_daily_returns = strategy_portval.pct_change()
    benchmark_daily_returns = benchmark_portval.pct_change()

    strategy_adr = strategy_daily_returns.mean()
    benchmark_adr = benchmark_daily_returns.mean()

    strategy_std_dev_daily_returns = strategy_daily_returns.std()
    benchmark_std_dev_daily_returns = benchmark_daily_returns.std()

    # print("CR Strategy:", float(CR_strategy))
    # print("CR Benchmark:", float(CR_benchmark))
    #
    # print("STD Daily Returns Strategy", float(strategy_std_dev_daily_returns))
    # print("STD Daily Returns Benchmark", float(benchmark_std_dev_daily_returns))
    #
    # print("Mean Daily Returns Strategy", float(strategy_adr))
    # print("Mean Daily Returns Benchmark", float(benchmark_adr))

if __name__ == "__main__":
    test_manual_strategy_in_sample()
    test_manual_strategy_out_of_sample()
    exp1.run_experiment_1()
    exp2.run_experiment_2()

    # test_learner_strategy()



