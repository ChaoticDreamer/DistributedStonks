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
from ui.user_interface import set_title, get_risk_for_stock



if __name__ == "__main__":
	set_title()
	get_risk_for_stock()