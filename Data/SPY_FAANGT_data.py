# Importing Timeseries function from alpha_vantage SDK
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import os
from dotenv import load_dotenv
import time
from sys import exit

# Make function for collecting data from Alpha Vantage, so that module doesn't run when imported
def SPY_FAANGT_data():
    '''
    Parameters:
    None. Function collects 20+ years of FAANGT and SPY (SP500 ETF) price data

    *****************************************************************************************************************************************************
    Returns: 
    Returns .csv files into "Data/csv_files/" directory (overwrites/updates existing .csv of same name) and 2 dataframes
    1.) FAANGT_df : a dataframe of FAANGT stocks (20+ years of data) from AlphaVantage API calls
    2.) FAANGT_close_df : a dataframe of only the closing prices from FAANGT_df 
    3.) FAANGT_close_data.csv : .csv file of FAANGT_close_df
    4.) FAANGT_data.csv : .csv file of FAANGT_df
    '''

    # Load in API key
    load_dotenv()
    alpha_vantage_key = os.getenv('ALPHAVANTAGE_API_KEY')
    # Confirm the availability of your Mapbox API access token by checking its type
    if type(alpha_vantage_key) == type(''):
        print('Key is available. SPY and FAANGT data is now loading (~5 mins)...')
    else: 
        exit('Try loading key again')

    ts = TimeSeries(key = alpha_vantage_key, output_format='pandas') #Note 500 requests per day cap, 5 per min
    SPY_FAANGT_list=['SPY','FB','AAPL','AMZN','NFLX', 'GOOG', 'TSLA']
    SPY_FAANGT_df_list = [] #iniate df list for later concatenation
    SPY_FAANGT_close_df_list = [] #iniate df list for just close prices later concatenation
    for ticker in SPY_FAANGT_list:
        ticker_data, meta_data = ts.get_daily(symbol=ticker, outputsize='full') #using Alpha Vantage API to grab S&P 500 ETF (ticker symbol = SPY), gives 20+ years of price data
        ticker_data.columns = [ticker + ' open', ticker + ' high', ticker + ' low', ticker + ' close', ticker + ' volume'] #rename columns automatically
        SPY_FAANGT_df_list.append(ticker_data) #add dataframe to the list
        SPY_FAANGT_close_df_list.append(ticker_data[ticker + ' close']) # Just the 'close' column
        time.sleep(25) #Note 500 requests per day cap, 5 per min

    SPY_FAANGT_df = pd.concat(SPY_FAANGT_df_list, axis=1, join='outer')
    SPY_FAANGT_close_df = pd.concat(SPY_FAANGT_close_df_list, axis=1, join='outer')

    # These directories will work only when called as function in Project Moon Notebook (DO NOT RUN in this notebook if in DATA/ directory or subdirs)
    SPY_FAANGT_close_df.to_csv('Data/csv_files/SPY_FAANGT_close_data.csv') 
    SPY_FAANGT_df.to_csv('Data/csv_files/SPY_FAANGT_data.csv')     

    return SPY_FAANGT_close_df

#Add a YYYY-MM-DD input so that data can be sliced to be same length in version 2.0