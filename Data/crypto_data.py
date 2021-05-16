# Importing necessary libraries
import pandas as pd
from pycoingecko import CoinGeckoAPI
import datetime
import time 
cg = CoinGeckoAPI()

# Create start and end time for CoinGeckoAPI
user_start_time = '2013-01-01'
user_end_time = '2021-05-14'

cg_start = datetime.datetime.strptime(user_start_time, "%Y-%m-%d")
cg_start = datetime.datetime.timestamp(cg_start)
cg_start = str(cg_start)

# if statement for user inputs now for present time, else they will input string in YYYY-mm-dd
if user_end_time == 'now':
    cg_end = datetime.datetime.now() #can allow users to enter in date time
    cg_end = datetime.datetime.timestamp(cg_end)
    cg_end = str(cg_end)
    
else:s
    cg_end = datetime.datetime.strptime(user_end_time, "%Y-%m-%d")
    cg_end = datetime.datetime.timestamp(cg_end)
    cg_end = str(cg_end)

#testing cg_start and cg_end variables for UNIX format
print(f'''UNIX start: {cg_start}      type{type(cg_start)}
UNIX end: {cg_end}      type {type(cg_end)}''') 

# List of dictionaries for each crypto...keys are 'id', 'symbol' etc...max per page is 250 so to get 500 coins and save results to variables cg_1, cg_2
cg_1 = cg.get_coins_markets(order='market_cap_desc', vs_currency='usd', per_page=250, page=1)
cg_2 = cg.get_coins_markets(order='market_cap_desc', vs_currency='usd', per_page=250, page=2)

#loop through data from CoinGecko stored in `cg_1` and `cg_2` using `cg.get_coin_markets` and save to list `coin_list` becasue limit of 
coin_list = []
for coin in cg_1:
    coin_list.append([coin['id'], coin['symbol'], coin['name'], coin['image'], coin['market_cap'], coin['market_cap_rank']])
    
for coin in cg_2:
    coin_list.append([coin['id'], coin['symbol'], coin['name'], coin['image'], coin['market_cap'], coin['market_cap_rank']])
    
coin_list_df = pd.DataFrame(coin_list, columns=['CG id','CG symbol', 'name', 'image', 'market_cap', 'market cap rank'])
coin_list_df
coin_list_df.to_csv('coin_list.csv')

# This is how to look up time when file is saved: https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
# can use this for decide if making api call is necessary

loop to create data frame from .csv file
coin_list_df = pd.read_csv('coin_list.csv')
# coin_list_df['CG id'][0:49] 
prices_dictionary = {}
df_list=[]#create an empty data frame list https://stackoverflow.com/questions/28910089/filling-empty-python-dataframe-using-loops


for CG_id in coin_list_df['CG id']:
    time.sleep(0.65) #adds a 0.65 second delay every call staying with in CoinGecko 100 calls/min (60 secs/100 calls) limit https://realpython.com/python-sleep/
    coin_API = cg.get_coin_market_chart_range_by_id( CG_id, 'usd', cg_start, cg_end) #API call to CoinGecko and grabing historical price data
    prices_dictionary[CG_id] = coin_API['prices'] # updating dictionary with CG_id as key and list o lists of unix time stamp and price data
    df_temp = pd.DataFrame(prices_dictionary[CG_id], columns=['time', CG_id+' prices']) #creating a temporary df that will later be appeneded into 
    df_temp['time'] = pd.to_datetime(df_temp['time'], origin='unix', unit='ms') #links (was having issue converting UNIX this helped https://github.com/pandas-dev/pandas/issues/10987)
    df_temp.set_index('time', inplace=True)
    df_list.append(df_temp)#append dataframe list in the loop
    
coin_historical_df = pd.concat(df_list, axis=1, join='outer') 
coin_historical_df.to_csv('crypto_price_data.csv')
# df['time'] = pd.to_datetime(df['time'], origin='unix', unit='ms') #links (was having issue converting UNIX this helped https://github.com/pandas-dev/pandas/issues/10987)

coin_historical_df
#LEFT OFF HERE...NEED TO FIGURE OUT HOW TO MAKE DICTIONARY WITH VALUES AS LIST OF LISTS INTO A DATAFRAME
