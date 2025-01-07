import datetime as dt
import os
import numpy as np
import pandas as pd
from util import get_data, plot_data
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import TheoreticallyOptimalStrategy as tos
import indicators as ids


def __init__(self):
    """
    Constructor method
    """
    pass  # move along, these aren't the drones you're looking for

def author(self):
    return "bkocan3"  # replace tb34 with your Georgia Tech username

if __name__ == "__main__":
    tos.testPolicy()
    ids.plot_bollinger_bands()
    ids.plot_momentum()
    ids.plot_rsi()
    ids.plot_macd()
    ids.plot_cci()