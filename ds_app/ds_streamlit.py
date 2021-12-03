# This file is part of ds_app.
#
# Developed for the Code With Me Distributed Stonks Project.
#
import pathlib
import sys

# This adds the path of the …/src folder
# to the PYTHONPATH variable
sys.path.append(str(pathlib.Path().absolute()).split("/ds_app")[0] + "/ds_app")

import streamlit as st
import ui.user_interface as ui

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
        <font size="9" face ="verdana" color ="lightblue" margin:5px>Distributed Stoncks </br> Risk Evaluator</font>
    </i>  
</h1> 
<img src="https://res.cloudinary.com/emerline/image/upload/v1605796379/zj4tre4h0yf3eefwg8u7.jpg" alt="res.cloudinary.com">     
</body>
</html>"""

st.write(HTML,unsafe_allow_html=True)

if __name__ == "__main__":
   ui.get_ticker_input()