# Project_Moon
This is a Jupyter Notebook application that allows one to quickly compare stocks (S&P 500 index funds, FAANGT stocks) to the top 500 peforming cryptos to help introduce investors to the world of cryptocurrencies outside of Bitcoin and Ethereum (also known as "alt coins") and the potential risks-return profile of the top performing cryptocurrencies. 

---


## Technologies

This project leverages python 3.7 with the following packages:

* [Pandas](https://pandas.pydata.org/docs/user_guide/visualization.html) - For data manipulation operations such as merging, sorting, selecting, as well as data cleaning features.

* [JupyterLab](http://jupyterlab.io/) -  For interactive user workspace providing user command line interface, help page, and entrypoint to the project.

* [matplotlib](https://plotly.com/python/px-arguments/) - Python package used to build plots. Input data arguments accepted by Plotly Express functions.

* [Numpy](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html) - NumPy sqrt function. Return the non-negative square-root of an array, element-wise. The values whose square-roots are required.

* [dotenv](https://www.npmjs.com/package/dotenv)- loads environment variables from a .env file into process.env.

* [CoinGeckoAPI](https://www.coingecko.com/en/api)- allows to retrieve cryptocurrency data such as price, volume, market cap, and exchange data. Sign up and register.

* [Alpha_Vantage](https://www.alphavantage.co/support/#api-key)- allows to retrieve stock data such as price, volume, market cap, and exchange data. Sign up and register.
---

## Installation Guide

Before running the application first install the following dependencies in your designated environment.


* [Git Bash (Windows) or Terminal (macOS)] (https://git-scm.com/downloads) -  
* [Anaconda with Python 3.7] (https://docs.anaconda.com/anaconda/install/) - 
* [installing the Requests library] (conda install -c anaconda requests)
* [installing the JSON library] (conda install -c jmcmurray json)
* [installing python-dotenv Library] (pip install python-dotenv)


--- 

You???ll use environment (.env) files to protect your CoinGeckoAPI and Alpha Vantage API keys. When you create an environment file, the system hides it in the folder structure of the project. 
Very important that you save your API key from Alpha Vantage in .env file and store in the Project_Moon folder in the following format:
ALPHAVANTAGE_API_KEY = "PASTE_YOUR_KEY_HERE".

Windows Users: Display Your Hidden Files in File Explorer
To display the hidden files on a Windows computer, complete the following steps:

In the search bar, type ???folder???.

Click ???File Explorer Options???.

In the ???File Explorer Options??? dialog box that displays, click the View tab. Select ???Show hidden files, folders, and drives,??? and then click OK
---



---

## Usage

To use Project_Moon book simply clone the repository and run "Git Bash" to open terminal to the correct directory:
![image](https://user-images.githubusercontent.com/38775809/119299037-12c17180-bc13-11eb-93a1-1d737d1df164.png)

- Start by activating an Anaconda Environment instance.
- Then start Jupyter Lab and open the Project_Moon.ipynb file
![image](https://user-images.githubusercontent.com/38775809/119300176-2a99f500-bc15-11eb-9749-a9e6906e4c63.png)

- Simply hit play and follow along to perform analysis.


---

## Contributors

Brought to you by:
- Matthew Ogbuehi, you may reach me at matt.ogbuehi@gmail.com
- Carlos R. you may reach me at reachcarlostoday@gmail.com

---

## License

MIT.
