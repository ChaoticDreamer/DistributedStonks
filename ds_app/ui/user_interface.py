# This file is part of ui.
#
# Developed for the Code With Me Distributed Stonks Project.
#
from risk.risk_beta import est_risk
import streamlit as st

def get_risk_for_stock():
	if est_risk() == "High":
	   st.title("Stock Overvalued")

def set_title():
	st.title("Distributed Stoncks Risk Evaluator")
	st.text_input("Enter the stock name for risk assessment")

if __name__ == "__main__":
	est_risk()