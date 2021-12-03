# This file is part of ui.
#
# Developed for the Code With Me Distributed Stonks Project.
#
import re
from risk.risk_fairvalue import evaluate_ticker
import streamlit as st
import pandas as pd

def get_ticker_input():
   
   ticker_input = st.sidebar.text_input(label="Please Enter Company's Ticker:",value="")

   if(st.sidebar.button("Submit") and ticker_input!=""):
      check_and_evaluate_ticker_input(ticker_input)
      
def check_and_evaluate_ticker_input(ticker_input):	
   
   ticker=ticker_input.title().lower()

   if re.search(r"\d",ticker) or re.search(r"\W",ticker):
      st.error("Ticker entered is invalid. Please Enter Correctly the Company's Ticker")   
   else:
      currentValue, fairValue, stockAssessment = evaluate_ticker(ticker)
      format_stockAssessment = format_text_color(stockAssessment)

      stock_pdf = pd.DataFrame([(ticker,currentValue,fairValue,stockAssessment)],
      	columns=('Ticker','Current Value', 'Fair Value', 'Stock Valuation'))

      styler = stock_pdf.style.hide_index().applymap(lambda x:format_stockAssessment, subset=['Stock Valuation'])
      st.markdown("""### **Company's Stock Evaluation using Fair Value Estimator**""")    
      st.write(styler.to_html(), unsafe_allow_html=True)

def format_text_color(stockAssessment):

   if stockAssessment=='Overvalued':
      color = 'font-family: "Times New Roman", Times, serif; color: #e83e8c; font-size:1.3em;'
   elif stockAssessment=='Undervalued':
      color = 'font-family: "Times New Roman", Times, serif; color: #3ee845; font-size:1.3em;'           
   else: 
      color = 'font-family: "Times New Roman", Times, serif; color: #7a7a7a; font-size:1.3em;'      
   
   return color


if __name__ == "__main__":
   get_ticker_input()