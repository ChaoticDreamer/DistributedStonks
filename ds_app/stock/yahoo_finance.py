# This file is part of stock.
#
# Developed for the Code With Me Distributed Stonks Project.
#

import yahoo_fin.stock_info as si


def get_info(stock_ticker):
   stock = si.get_data(stock_ticker)
   print(stock)




if __name__ == "__main__":
	get_info("MSFT")
	