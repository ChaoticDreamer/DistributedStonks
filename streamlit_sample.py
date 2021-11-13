# Program shows if a Company is UnderValued Or OverValued
#

import streamlit as st
import pandas as pd
from pytz import timezone
from datetime import date, timedelta, datetime
import time
import sys
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
def get_quote_tableData(ticker):
    try:
        stockQuote_dict = si.get_quote_table(ticker)
        pdf = pd.DataFrame([(ticker,stockQuote_dict["Beta (5Y Monthly)"], stockQuote_dict["EPS (TTM)"], stockQuote_dict["PE Ratio (TTM)"])],
                columns=('Ticker','Beta(5Y Monthly)', 'EPS (TTM)', 'P/E Ratio (TTM)'))          
    except:
        e=sys.exc_info()[0]
        # Wait for 15 seconds, then try call again in case of Network hicup
        time.sleep(15)
        stockQuote_dict = si.get_quote_table(ticker)
        pdf = pd.DataFrame([(ticker,stockQuote_dict["Beta (5Y Monthly)"], stockQuote_dict["EPS (TTM)"], stockQuote_dict["PE Ratio (TTM)"])],
                columns=('Ticker','Beta(5Y Monthly)', 'EPS (TTM)', 'P/E Ratio (TTM)'))
        raise e
        #currentVolume = stockQuote_dict['Volume']
    
    return pdf

def getuserStockInput(ticker):#{
    try:
        stockQuote_df = get_quote_tableData(ticker) 
        st.markdown("# Company's Financial Dashboard")
        st.dataframe(stockQuote_df)
    except:
        e=sys.exc_info()[0]
        st.error(f"Exception Thrown:si.get_quote_table{e}:Enter Valid Company's Ticker")    
   
def main(): 
    ticker_input = st.sidebar.text_input(label="Please Enter Company's Ticker:",value="")
    if(st.sidebar.button("Submit") and ticker_input!=""):
        ticker=ticker_input.title().lower()
        getuserStockInput(ticker)
        #Debugging Code
        #st.sidebar.success(ticker)
    
    #Debugging Code
    #aapl_df = si.get_data("aapl")
    #st.dataframe(aapl_df)


st.write(HTML,unsafe_allow_html=True)
if __name__ == '__main__':
    main()    


