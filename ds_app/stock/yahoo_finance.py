# This file is part of stock.
#
# Developed for the Code With Me Distributed Stonks Project.
#
import yahoo_fin.stock_info as si

class CompanyInfo:
	
   def __init__(self,ticker):
      try:
         self.ticker=ticker
         self.price_df = si.get_data(self.ticker) 
         self.overview_df = si.get_stats(self.ticker) 
         self.get_earnings = si.get_earnings(self.ticker)
         self.get_financials = si.get_financials(self.ticker)
         self.get_quote_data = si.get_quote_data(self.ticker)
         self.get_stats_df = si.get_stats(self.ticker)
         self.get_stats_valuation = si.get_stats_valuation(self.ticker)
         self.overviewQuote_dict = si.get_quote_table(self.ticker)        
         self.income_statement_df = si.get_income_statement(self.ticker)
         self.balance_sheet_df = si.get_balance_sheet(self.ticker)
         self.cash_flows_df = si.get_cash_flow(self.ticker)  
      except:
         e=sys.exc_info()[0]
         # Wait for 5 seconds, then try call again in case of Network hicup
         #time.sleep(5)
         raise e

       
if __name__ == "__main__":
   msft_stock = CompanyInfo('msft')
   print(msft_stock.overview_df)	