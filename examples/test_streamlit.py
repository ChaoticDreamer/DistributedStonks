"""
# My first app
Example using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
from myconfig.myconfig import set_title

set_title()
#st.title("Distributed Stoncks Risk Evaluator")
st.text_input("Enter the stock name for risk assessment")

#st.write(pd.DataFrame({
#  'first column': [1, 2, 3, 4],
#  'second column': [10, 20, 30, 40]
#}))
dataframe = pd.DataFrame(
	np.random.randn(10,20),
	columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


