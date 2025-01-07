import matplotlib.pyplot as plt
import StrategyLearner as sl
import marketsimcode as mktsim
import datetime as dt
from util import get_data
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
import pandas as pd
register_matplotlib_converters()
def conduct_experiment(impact_values, symbol, sd, ed, sv=100000):
    metrics = {'cumulative_return': [], 'average_daily_return': []}

    for impact in impact_values:
        # Initialize StrategyLearner with a specific impact
        learner = sl.StrategyLearner(impact=impact, commission=0.00)
        learner.add_evidence(symbol=symbol, sd=sd, ed=ed, sv=sv)
        df_trades = learner.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=sv)
        orders = []
        for date, row in df_trades.iterrows():
            if row[symbol] != 0:
                order_type = 'BUY' if row[symbol] > 0 else 'SELL'
                shares = abs(int(row[symbol]))
                orders.append([symbol, order_type, shares])

        orders_df = pd.DataFrame(orders, columns=['Symbol', 'Order', 'Shares'])
        orders_df.index = df_trades[df_trades[symbol] != 0].index

        portvals = mktsim.compute_portvals(sd, ed, orders_df, start_val=sv, commission=0.00, impact=impact)

        # Calculate metrics
        cumulative_return = (portvals.iloc[-1] / portvals.iloc[0]) - 1
        daily_returns = portvals.pct_change(1).iloc[1:]
        average_daily_return = daily_returns.mean()

        # Store metrics
        metrics['cumulative_return'].append(cumulative_return)
        metrics['average_daily_return'].append(average_daily_return)

        # Plot the portfolio values
        plt.plot(portvals, label=f'Impact: {impact}')

    return metrics

def run_experiment_2():
    # Experiment parameters
    symbol = 'JPM'
    sd = dt.datetime(2008, 1, 1)
    ed = dt.datetime(2009, 12, 31)
    impact_values = [0.0, 0.005, 0.01]

    # Conduct the experiment
    metrics = conduct_experiment(impact_values, symbol, sd, ed)

    # Plot settings
    plt.title('Strategy Learner Portfolio Value Across Different Impacts')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.plot()
    # plt.show()
    plt.savefig("./images/exp-2-varying-impacts.png")
    plt.clf()

    # Print metrics
    for impact, cum_ret, avg_daily_ret in zip(impact_values, metrics['cumulative_return'], metrics['average_daily_return']):
        print(f"Impact: {impact}, Cumulative Return: {cum_ret}, Average Daily Return: {avg_daily_ret}")

if __name__ == "__main__":
    run_experiment_2()
