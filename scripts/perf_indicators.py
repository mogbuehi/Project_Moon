# Import Pandas library 
import pandas as pd
# Import the Path module from the pathlib library
from pathlib import Path
# Import the NumPy library
import numpy as np


def get_crypto_coins(): # Make function for collecting data from Coin Gecko, so that module doesn't run when imported

# Using the read_csv function and the Path module, read in the "crypto_price_data.csv" file from the Resources folder
# Set the "date" as the index column 
# Be sure to set the DatetimeIndex using the parse_dates and infer_datetime_format parameters
    crypto_coins_df = pd.read_csv(
        Path("/Users/craymundo/Documents/GitHub/Project_Moon/Data/crypto_price_data.csv"), 
        index_col="time", 
        infer_datetime_format=True, 
        parse_dates=True
    )
    return crypto_coins_df



#********************************************************************#
# ** Perfomance indicators **  - Percentage change.
def get_pct_change(crypto_coins_df): # Make function for collecting data from Coin Gecko, so that module doesn't run when imported
# Using the Pandas pct_change function in conjunction with the dropna function, generate the tech daily returns DataFrame
#alt_bitcoin_daily_returns = crypto_coins_df.pct_change().dropna()
    crypto_daily_returns_df = crypto_coins_df.pct_change()
    return crypto_daily_returns_df
# ** Perfomance indicators **  - Cumulative percent returns.
def get_cumulative_prod(crypto_daily_returns_df):
# Calculating and ploting the cumulative returns including BTC
# Using the Pandas cumprod function and the cumulative returns equation to generate the cumulative daily returns DataFrame 
    get_cumulative_prod_df = (1 + crypto_daily_returns_df).cumprod()
# Reviewing the last 5 rows of whales cumulative daily returns DataFrame
    return get_cumulative_prod_df
# ** Perfomance indicators **  - Rolling mean.
# ** Perfomance indicators **  - Rolling mean returns.
#********************************************************************#

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# ++ Volatility ++ - Standard deviation.
def get_standard_deviation(crypto_daily_returns_df):
# Calculating and sort the standard deviation for all ALT coins
# Displaying the standard deviations sorted smallest to largest
    standard_deviation_df = crypto_daily_returns_df.std().sort_values()  
# Sorting the annual standard deviations for the cryptocurrencies from lowest to highest
#standard_deviation.sort_values()
    return standard_deviation_df
# ++ Volatility ++ - Annualized Standard deviation.

# ++ Volatility ++ - Rolling Standard deviation.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#********************************************************************#
# ** Risk-Return **  - Beta(60 day rolling covariance).
def get_standard_deviation(crypto_daily_returns_df):

# Calculating the variance using a 60-day rolling window
    #snp_rolling_60_variance = crypto_daily_returns_df['S&P 500'].rolling(window=60).var()
    beta_rolling_60_variance = crypto_daily_returns_df.rolling(window=60).var()
# Calculating the covariance using a 60-day rolling window
    #beta__rolling_60_covariance = crypto_daily_returns_df['BERKSHIRE HATHAWAY INC'].rolling(window=60).cov(crypto_daily_returns_df['S&P 500'])
    beta__rolling_60_covariance = crypto_daily_returns_df.rolling(window=60).cov(crypto_daily_returns_df)
# Calculating the beta based on the 60-day rolling covariance compared to the S&P 500
    rolling_60_beta_df = beta__rolling_60_covariance / beta_rolling_60_variance
    return rolling_60_beta_df

# ** Risk-Return **  - Sharpe.
def get_sharpe_rations(standard_deviation_df,crypto_daily_returns_df):
# The number of trading days is set to 252 for use throughout these calculations
    trading_days = 252
# Calculate the annualized standard deviation for the fund portfolios and the S&P 500
# Use the Pandas std function to calculate the standard deviation
# Multiply the standard deviation by the square root (using the NumPy sqrt function) of the number of trading days
    annual_average_return = crypto_daily_returns_df.mean() * np.sqrt(trading_days)

# Calculating and sorting the annualized standard deviation (252 trading days) of the 4 portfolios and the S&P 500
# Displaying the annual standard deviations smallest to largest
    annual_standard_deviation = standard_deviation_df * np.sqrt(trading_days)
   

# Calculate Sharpe ratios by dividing the annual average return of the fund portfolios and the S&P 500
# by the annual standard deviation
    sharpe_ratios_df = annual_average_return / annual_standard_deviation
    return sharpe_ratios_df

#********************************************************************#

