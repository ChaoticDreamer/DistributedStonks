# Program shows if a Company is UnderValued Or OverValued
#

import streamlit as st
import pandas as pd
from pytz import timezone
from datetime import date, timedelta, datetime
import time
import sys
import re
#from yahoo_fin.stock_info import *
import yahoo_fin.stock_info as si

HTML = """<!DOCTYPE html>
<html>
<head>
<title>Code_With_Me Using Python</title>
<style>
    h1{
        text-align: center;
    }
    img {
        width:100%;
        height:100%;
    } 
</style
</head>
<h1>
    <i> 
        <font size="9" face ="verdana" color ="lightblue" margin:5px>Code_With_Me </br>Using StreamLit</font>
    </i>  
</h1> 
<img src="https://res.cloudinary.com/emerline/image/upload/v1605796379/zj4tre4h0yf3eefwg8u7.jpg" alt="res.cloudinary.com">     
</body>
</html>"""

#days=2*365=2 Years; datetime.now(timezone('America/New_York'))
#@st.cache
class CompanyStockInfo:#{
    def __init__(self,ticker):#{
        try:#{
            self.ticker=ticker
            #self.price_df=si.get_data(ticker,datetime.now(timezone('America/New_York')) - timedelta(days=365), datetime.date(datetime.now(timezone('America/New_York')))) 
            self.price_df = si.get_data(self.ticker) 
            #self.price_df = si.get_data(ticker,datetime.now(timezone('America/New_York')) - timedelta(days=1), datetime.date(datetime.now(timezone('America/New_York')))) 
            self.overview_df = si.get_stats(self.ticker) 
            # Misc data
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
        
    def getStatsColor(self,currentprice,fairVal):#{    
        try:
            self.fairVal=fairVal
            self.currentprice=currentprice
            color = ''
            if(self.currentprice > self.fairVal):
                color= 'font-family: "Times New Roman", Times, serif; color: #e83e8c; font-size:1.3em;'
            
            elif(self.currentprice < self.fairVal):
                color = 'font-family: "Times New Roman", Times, serif; color: #3ee845; font-size:1.3em;'           
           
            else: 
                color = 'font-family: "Times New Roman", Times, serif; color: #7a7a7a; font-size:1.3em;'      
        
        except:
            e=sys.exc_info()[0]
            raise e
       
        return color


def getCompanyObject(ticker):#{
    count = 0 # Count Retry Call
    waitTime = 5 #Wait 5 seconds
    company = None 
    while count <= 3:#{  # try 3 times
        try:#{
            company = CompanyStockInfo(ticker)
            break
        
        except:#{
            e=sys.exc_info()[0]
            # If trying 3rd time and still error?? 
            # Just throw the error- we don't have anything to hide :)
            if count == 3:
                raise e 
              
            time.sleep(waitTime)    
            count += 1              
     
    return company


def main():
     try:
        ticker_input=None
        company=None
        ticker=None
        pdf=None
        fairVal=None
        currentprice=None
        # st.sidebar.markdown("# Please Enter Company's Ticker:")
        ticker_input = st.sidebar.text_input(label="Please Enter Company's Ticker:",value="")
        #btnSubmit = st.sidebar.button("Submit")

        if(st.sidebar.button("Submit") and ticker_input!=""):
            # When Search Button is Clicked, Get Input_Text Ticker String
            ticker=ticker_input.title().lower()    
            if re.search(r"\d",ticker) or re.search(r"\W",ticker):
                st.error("Enter Valid Company's Ticker")   
            else:
                company=getCompanyObject(ticker)
                 
            st.write(company.get_stats_valuation)
            st.write(company.overviewQuote_dict)
            evalStockValuation = ["OverValued","UnderValued","FairValued"]
            pdf = pd.DataFrame([(ticker,company.overviewQuote_dict["Beta (5Y Monthly)"], company.overviewQuote_dict["EPS (TTM)"], company.overviewQuote_dict["PE Ratio (TTM)"])],
                columns=('Ticker','Beta(5Y Monthly)', 'EPS (TTM)', 'P/E Ratio (TTM)')) 
            table = company.get_stats_valuation.iloc[:,:2]
            table.columns = ["Attribute", "RecentValue"]
                
            fairVal = (float(table[table.Attribute.str.contains("Forward P/E")].iloc[0,1]) *
                       float(table[table.Attribute.str.contains("PEG Ratio")].iloc[0,1]))/2
                           
            currentprice = company.overviewQuote_dict["Quote Price"]
                
            if(currentprice > fairVal):
                pdf["StockValuation"] = evalStockValuation[0]
            elif(currentprice < fairVal):
                pdf["StockValuation"] = evalStockValuation[1]                       
            else:
                pdf["StockValuation"] = evalStockValuation[2]                   

  
            st.write(currentprice)
            st.write(fairVal)
            props=company.getStatsColor(currentprice,fairVal)
            st.markdown("""### **Company's Stock Evaluation**""")
            st.dataframe(pdf.style.applymap(lambda x: props, subset=["StockValuation"]))
                                    
     except:#{
         e=sys.exc_info()[1]
         st.error(f"An error occurred while connecting To Yahoo Finance Please Try Again:{e}")
         #raise e
    #}      
#}//end main
st.write(HTML,unsafe_allow_html=True)
if __name__ == '__main__':#{
    main()    
#}//end main()