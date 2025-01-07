import pandas as pd
from pandas.plotting import register_matplotlib_converters
from util import get_data
from indicators import calculate_bollinger_bands, calculate_rsi, calculate_macd
register_matplotlib_converters()

class ManualStrategy:
    def __init__(self):
        pass

    def testPolicy(self, symbol, sd, ed, sv):
        # Load price data
        dates = pd.date_range(sd, ed)
        prices = get_data([symbol], dates)[symbol]

        # Calculate indicators
        bb = calculate_bollinger_bands(symbol, sd, ed)
        rsi = calculate_rsi(symbol, sd, ed)
        macd = calculate_macd(symbol, sd, ed)

        # Create a DataFrame to store trades
        trades = pd.DataFrame(index=prices.index, columns=[symbol])
        trades[symbol] = 0

        # Define thresholds for indicators
        bb_buy_threshold = 0.3
        bb_sell_threshold = 0.7
        rsi_buy_threshold = 35
        rsi_sell_threshold = 65
        macd_buy_threshold = -0.5
        macd_sell_threshold = 0.5

        # Initialize previous position
        prev_position = 0

        # Apply trading rules
        for i in range(1, len(prices)):
            # Determine the signal
            signal = 0
            if bb.iloc[i] < bb_buy_threshold and rsi.iloc[i] < rsi_buy_threshold and macd.iloc[i] > macd_buy_threshold:
                signal = 1  # Long
            elif bb.iloc[i] > bb_sell_threshold and rsi.iloc[i] > rsi_sell_threshold and macd.iloc[i] < macd_sell_threshold:
                signal = -1  # Short

            # Determine the trade based on the signal and previous position
            if signal == 1 and prev_position <= 0:  # Buying
                trades[symbol].iloc[i] = 1000 - prev_position
                prev_position = 1000
            elif signal == -1 and prev_position >= 0:  # Selling
                trades[symbol].iloc[i] = -1000 - prev_position
                prev_position = -1000
            # No change in position
            else:
                trades[symbol].iloc[i] = 0

        orders = []
        for date, row in trades.iterrows():
            if row[symbol] != 0:
                order_type = 'BUY' if row[symbol] > 0 else 'SELL'
                shares = abs(int(row[symbol]))
                orders.append([symbol, order_type, shares])

        orders_df = pd.DataFrame(orders, columns=['Symbol', 'Order', 'Shares'])
        orders_df.index = trades[trades[symbol] != 0].index  # Assigning the trade dates as index
        # print(orders_df)
        return trades