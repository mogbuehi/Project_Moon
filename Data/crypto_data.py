# Importing necessary libraries
import pandas as pd
from pycoingecko import CoinGeckoAPI
import datetime
import time 
cg = CoinGeckoAPI()

user_start_time = '2013-01-01'
user_end_time = '2021-05-14'

def crypto_data_collector(user_start_time, user_end_time): # Make function for collecting data from Coin Gecko, so that module doesn't run when imported
    '''Args:
    user_start_time = string in "YYYY-MM-DD" format
    user_end_time = string in "YYYY-MM-DD" format or "today" (which will return present day)

    Returns: 2 .csv files into "Data/ directory" (overwrites/updates existing .csv of same name) and a dataframe
        1.) "coin_list.csv" : a list of the top 500 cryptos, from highest market cap to lowest market cap with id, symbol, image url, market cap, 
        and rank from CoinGecko
        2.) "crypto_price_data.csv" : a list of daily closing prices of the top 500 (market cap) cryptos
        3.) `coin_historical_df`: a data frame of of the top 500 (market cap) cryptos' closing prices from `user_start_time` to `user_end_time`, 
        with datetime index
    '''
    # Create start and end time for CoinGeckoAPI
    
    cg_start = datetime.datetime.strptime(user_start_time, "%Y-%m-%d")
    cg_start = datetime.datetime.timestamp(cg_start)
    cg_start = str(cg_start)

    # if statement for user inputs now for present time, else they will input string in YYYY-mm-dd
    if user_end_time == 'today':
        cg_end = datetime.datetime.now() #can allow users to enter in date time
        cg_end = datetime.datetime.timestamp(cg_end)
        cg_end = str(cg_end)

    else:
        cg_end = datetime.datetime.strptime(user_end_time, "%Y-%m-%d")
        cg_end = datetime.datetime.timestamp(cg_end)
        cg_end = str(cg_end)

    # List of dictionaries for each crypto...keys are 'id', 'symbol' etc...max per page is 250 so to get 500 coins and save results to variables cg_1, cg_2
    cg_1 = cg.get_coins_markets(order='market_cap_desc', vs_currency='usd', per_page=250, page=1)
    cg_2 = cg.get_coins_markets(order='market_cap_desc', vs_currency='usd', per_page=250, page=2)

    #loop through data from CoinGecko stored in `cg_1` and `cg_2` using `cg.get_coin_markets` and save to list `coin_list` becasue limit of 
    coin_list = []
    for coin in cg_1:
        coin_list.append([coin['id'], coin['symbol'], coin['name'], coin['image'], coin['market_cap'], coin['market_cap_rank']])

    for coin in cg_2:
        coin_list.append([coin['id'], coin['symbol'], coin['name'], coin['image'], coin['market_cap'], coin['market_cap_rank']])
    
    # Organize and clean up df to include 
    coin_list_df = pd.DataFrame(coin_list, columns=['CG id','CG symbol', 'name', 'image', 'market_cap', 'market cap rank'])
    coin_list_df
    coin_list_df.to_csv('Data/coin_list.csv')
    print('coin_list.csv saved in Data/ folder, please wait ~10 mins while crypto_price_data is loading...')
    #load data to create data frame from .csv file
    coin_list_df = pd.read_csv('Data/coin_list.csv')
    prices_dictionary = {}
    df_list=[]#create an empty list for storing data frames https://stackoverflow.com/questions/28910089/filling-empty-python-dataframe-using-loops


    for CG_id in coin_list_df['CG id']:
        time.sleep(1) #adds a 1 second delay every call staying with in CoinGecko 100 calls/min (60 secs/100 calls) limit https://realpython.com/python-sleep/
        coin_API = cg.get_coin_market_chart_range_by_id( CG_id, 'usd', cg_start, cg_end) #API call to CoinGecko and grabing historical price data
        prices_dictionary[CG_id] = coin_API['prices'] # updating dictionary with CG_id as key and list o lists of unix time stamp and price data
        df_temp = pd.DataFrame(prices_dictionary[CG_id], columns=['time', CG_id+' prices']) # creating a temporary df that will later be appeneded into df_list
        df_temp['time'] = pd.to_datetime(df_temp['time'], origin='unix', unit='ms') #links (was having issue converting UNIX this helped https://github.com/pandas-dev/pandas/issues/10987)
        df_temp.set_index('time', inplace=True)
        df_list.append(df_temp)#append dataframe list in the loop

    coin_historical_df = pd.concat(df_list, axis=1, join='outer') 
    coin_historical_df.to_csv('Data/crypto_price_data.csv')
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------     
    return crypto_price_df



