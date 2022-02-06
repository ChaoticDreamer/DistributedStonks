# This file is part of meas.
#
# Developed for the Code With Me Distributed Stonks Project.
#
import pandas as pd
from stock.yahoo_finance import CompanyInfo
import streamlit as st

def evaluate_ticker(ticker):
   
   company = CompanyInfo(ticker)
   
   table = company.get_stats_valuation.iloc[:,:2]
   table.columns = ["Attribute", "RecentValue"]

   fairValue = _estimate_fairvalue(table)
   currentprice = company.overviewQuote_dict["Quote Price"]

   evalStockValuation = ["Overvalued","Undervalued","Fair value"]

   if(currentprice > fairValue):
       stockValuation = "Overvalued"
   elif(currentprice < fairValue):
       stockValuation = "Undervalued"                      
   else: 
       stockValuation = "Fair Value"
    
   return currentprice, fairValue, stockValuation

def _estimate_fairvalue(table):
   return(float(table[table.Attribute.str.contains("Forward P/E")].iloc[0,1]) *
                       float(table[table.Attribute.str.contains("PEG Ratio")].iloc[0,1]))/2
   
if __name__=="__main__":
	evaluate_ticker("msft")