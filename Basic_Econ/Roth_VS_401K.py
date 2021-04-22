import numpy as np
import matplotlib.pyplot as plt

from Econ_tools import Compound_interst_calc


monthly_deposite=300
yearly_interest=0.08
total_years=20

year,total_asset=Compound_interst_calc(monthly_deposite,total_years,yearly_interest,plot=True)

