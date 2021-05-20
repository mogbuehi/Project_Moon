# Import Pandas library 
import pandas as pd
# Import the Path module from the pathlib library
from pathlib import Path
# Import the NumPy library
import numpy as np


#********************************************************************#
# ** Perfomance indicators **  - Percentage change.
def get_pct_change(dataframe): # Make function for collecting data from Coin Gecko, so that module doesn't run when imported
# Using the Pandas pct_change function in conjunction with the dropna function, generate the tech daily returns DataFrame
#alt_bitcoin_daily_returns = crypto_coins_df.pct_change().dropna()
    pct_change_df = dataframe.pct_change(fill_method='bfill') #https://www.geeksforgeeks.org/python-pandas-series-pct_change/  may solve issue with Nan
    return pct_change_df
# ** Perfomance indicators **  - Cumulative percent returns.
def get_cumulative_returns(dataframe):
# Calculating and ploting the cumulative returns
# Using the Pandas cumprod function and the cumulative returns equation to generate the cumulative daily returns DataFrame 
    get_cumulative_returns_df = (1 + get_pct_change(dataframe)).cumprod()
# Reviewing the last 5 rows of whales cumulative daily returns DataFrame
    return get_cumulative_returns_df
# ** Perfomance indicators **  - Rolling mean.
# ** Perfomance indicators **  - Rolling mean returns.
#********************************************************************#

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# ++ Volatility ++ - Standard deviation.
def get_standard_deviation(dataframe):
# Calculating and sort the standard deviation for all ALT coins
# Displaying the standard deviations sorted smallest to largest
    standard_deviation_df = dataframe.fillna(0).std().sort_values()
# Sorting the annual standard deviations for the cryptocurrencies from lowest to highest
    return standard_deviation_df
# ++ Volatility ++ - Annualized Standard deviation.

# ++ Volatility ++ - Rolling Standard deviation.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#********************************************************************#
# ** Risk-Return **  - Beta(60 day rolling covariance).
def get_rolling_beta(asset_df, market_df, days=60):

# Calculating the variance using a  rolling window (default is 60-day)
    #beta = cov(asset_df, market_df)/var(market_df)
# Calculating the rolling covariance 
    rolling_variance = market_df.rolling(window=days).var()
    rolling_covariance = asset_df.pct_change().rolling(window=days).cov(market_df)
# Calculating the rolling beta 
    rolling_beta_df = rolling_covariance / rolling_variance
    return rolling_beta_df

# ** Risk-Return **  - Sharpe.
def get_sharpe_ratios(dataframe, trading_days = 252):
# The number of trading days is set to 252 for use throughout these calculations, though crypto generally trade 365 days a year
# Calculate the annualized standard deviation for the fund portfolios and the S&P 500
# Use the Pandas std function to calculate the standard deviation
# Multiply the standard deviation by the square root (using the NumPy sqrt function) of the number of trading days
    annualized_average_return = dataframe.mean() * (trading_days)

# Calculating and sorting the annualized standard deviation (252 trading days)
    annualized_standard_deviation = get_standard_deviation(dataframe) * np.sqrt(trading_days)

# Calculate Sharpe ratios by dividing the annual average return of the fund portfolios and the S&P 500
# by the annual standard deviation
    sharpe_ratios_df = annualized_average_return / annualized_standard_deviation
    
    return sharpe_ratios_df

#********************************************************************#

