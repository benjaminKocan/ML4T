import matplotlib.pyplot as plt
import pandas as pd
from util import get_data

def author(self):
    return "bkocan3"  # replace tb34 with your Georgia Tech username

def calculate_momentum(symbol="JPM", sd="2008-01-01", ed="2009-12-31", lb=20):
    # Fetch the prices
    dates = pd.date_range(sd, ed)
    prices = get_data([symbol], dates)[symbol]

    # Calculate Momentum
    momentum = (prices / prices.shift(lb)) - 1
    return momentum

    # plt.figure(figsize=(12, 6))
    #
    # # Plot momentum
    # plt.plot(momentum, label='Momentum', color='black')
    #
    # # Add title and labels
    # plt.title(f"Momentum for {symbol}")
    # plt.xlabel("Date")
    # plt.ylabel("Momentum")
    #
    # # Highlight regions where momentum is positive in green, and negative in red
    # plt.fill_between(momentum.index, momentum, where=(momentum > 0), color='g', alpha=0.5, label='Buy Signal')
    # plt.fill_between(momentum.index, momentum, where=(momentum < 0), color='r', alpha=0.5, label='Sell Signal')
    #
    # # Add legend
    # plt.legend()
    # plt.grid(True)
    # plt.tight_layout()
    # plt.savefig("./images/momentum.png")
    # plt.clf()


def calculate_bollinger_bands(symbol="JPM", sd="2008-01-01", ed="2009-12-31", window=20):
    dates = pd.date_range(sd, ed)
    prices = get_data([symbol], dates)[symbol]

    sma = prices.rolling(window=window).mean()
    rolling_std = prices.rolling(window=window).std()
    upper_band = sma + (2 * rolling_std)
    lower_band = sma - (2 * rolling_std)
    bbp = (prices - lower_band) / (upper_band - lower_band)
    return bbp


    # buy_signals = (prices < lower_band) & (prices.shift(1) >= lower_band)
    # sell_signals = (prices > upper_band) & (prices.shift(1) <= upper_band)
    #
    #
    # plt.figure(figsize=(12, 6))
    # plt.plot(prices, label=symbol, color='black')
    # plt.plot(sma, label='SMA', color='blue', linestyle='--')
    # plt.plot(upper_band, label='Upper Band', color='green')
    # plt.plot(lower_band, label='Lower Band', color='red')
    #
    # plt.plot(prices[buy_signals], 'o', markersize=5, color='g', label="Buy Signal")
    # plt.plot(prices[sell_signals], 'o', markersize=5, color='r', label="Sell Signal")
    #
    # plt.title(f"Bollinger Bands for {symbol}")
    # plt.xlabel("Date")
    # plt.ylabel("Price")
    # plt.legend()
    # plt.grid(True)
    # plt.tight_layout()
    # plt.savefig("./images/bollinger_bands.png")
    # plt.clf()

def calculate_rsi(symbol="JPM", sd="2008-01-01", ed="2009-12-31", window=14):
    dates = pd.date_range(sd, ed)
    prices = get_data([symbol], dates)[symbol]

    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

    # plt.figure(figsize=(12, 6))
    # plt.plot(rsi, label="RSI", color="black")
    # plt.fill_between(rsi.index, rsi, 70, where=(rsi > 70), color='red', interpolate=True, alpha=0.5)
    # plt.fill_between(rsi.index, rsi, 30, where=(rsi < 30), color='green', interpolate=True, alpha=0.5)
    # plt.axhline(70, color="red", linestyle="--")
    # plt.axhline(30, color="green", linestyle="--")
    #
    # # Add labels for Overbought and Oversold
    # plt.text(rsi.index[0], 72, 'Overbought', color='red', va='center', ha='left', backgroundcolor='white')
    # plt.text(rsi.index[0], 28, 'Oversold', color='green', va='center', ha='left', backgroundcolor='white')
    #
    # plt.title("RSI with Overbought & Oversold Indicators for " + symbol)
    # plt.legend()
    # plt.grid(True)
    # plt.tight_layout()
    # plt.savefig("./images/rsi.png")
    # plt.clf()


def calculate_macd(symbol="JPM", sd="2008-01-01", ed="2009-12-31"):
    dates = pd.date_range(sd, ed)
    prices = get_data([symbol], dates)[symbol]

    ema_12 = prices.ewm(span=12, adjust=False).mean()
    ema_26 = prices.ewm(span=26, adjust=False).mean()
    macd = ema_12 - ema_26
    # signal_line = macd.ewm(span=9, adjust=False).mean()
    return macd

    # plt.figure(figsize=(12, 6))
    # plt.plot(macd, label="MACD", color="black")
    # plt.plot(signal_line, label="Signal Line", color="orange")
    #
    # plt.fill_between(macd.index, macd, signal_line, where=(macd > signal_line), color='g', alpha=0.3, label="Buy Region")
    # plt.fill_between(macd.index, macd, signal_line, where=(macd < signal_line), color='r', alpha=0.3, label="Sell Region")
    #
    # plt.title(f"MACD and Signal Line for {symbol}")
    # plt.xlabel('Date')
    # plt.ylabel('Value')
    # plt.legend()
    # plt.tight_layout()
    # plt.grid(True)
    # plt.savefig("./images/macd.png")
    # plt.clf()

def calculate_cci(symbol="JPM", sd="2008-01-01", ed="2009-12-31", window=20):
    dates = pd.date_range(sd, ed)
    prices = get_data([symbol], dates)[symbol]

    approx_high = prices.rolling(window=window).max()
    approx_low = prices.rolling(window=window).min()

    typical_price = (approx_high + approx_low + prices) / 3
    moving_avg = typical_price.rolling(window=window).mean()
    mean_deviation = typical_price.rolling(window=window).apply(lambda x: abs(x - x.mean()).mean(), raw=True)

    # CCI
    cci = (typical_price - moving_avg) / (0.015 * mean_deviation)
    return cci

    # plt.figure(figsize=(12, 6))
    # plt.plot(cci, label='CCI', color='black')
    #
    # plt.fill_between(cci.index, cci, 100, where=(cci > 100), color='red', interpolate=True, alpha=0.5, label='Sell Signal')
    # plt.fill_between(cci.index, cci, -100, where=(cci < -100), color='green', interpolate=True, alpha=0.5, label='Buy Signal')
    #
    # plt.axhline(100, color='red', linestyle='--')
    # plt.axhline(-100, color='green', linestyle='--')
    #
    # # Add labels for Overbought and Oversold
    # plt.text(cci.index[0], 105, 'Overbought', color='red', va='center', ha='left', backgroundcolor='white')
    # plt.text(cci.index[0], -105, 'Oversold', color='green', va='center', ha='left', backgroundcolor='white')
    #
    # plt.title(f'Commodity Channel Index (CCI) for {symbol}')
    # plt.xlabel('Date')
    # plt.ylabel('CCI Value')
    # plt.legend()
    # plt.grid(True)
    # plt.tight_layout()
    # plt.savefig("./images/cci.png")
    # plt.clf()










