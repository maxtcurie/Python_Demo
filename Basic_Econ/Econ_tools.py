import numpy as np
import matplotlib.pyplot as plt

def Compound_interst_calc(monthly_deposite,total_years,yearly_interest=0.08, tax_rate=0., plot=False):

	year=[]
	total_asset=[]
	total_asset_after_tax=[]
	total_asset_TEMP=0



	for i in range(int(total_years)*12):
		total_asset_TEMP=total_asset_TEMP*(1.+yearly_interest/12.)+monthly_deposite
		year.append(i/12.)
		total_asset.append(total_asset_TEMP/1000.)
		total_asset_TEMP=(total_asset_TEMP-(i+1.)*monthly_deposite)*(1.-tax_rate)+(i+1.)*monthly_deposite
		total_asset_after_tax.append(total_asset_TEMP/1000.)

	year=np.array(year)
	total_asset=np.array(total_asset)
	total_asset_after_tax=np.array(total_asset_after_tax)
	
	if plot==True:
		plt.clf()
		plt.plot(year,total_asset,label='before tax')
		plt.plot(year,total_asset_after_tax,label='after tax')
		plt.grid(color='black', linestyle='-', alpha=0.1, linewidth=0.5)
		plt.xlabel('year')
		plt.ylabel('total asset(k USD)')
		plt.show()
	
	return year,total_asset,total_asset_after_tax



'''
monthly_deposite=300
yearly_interest=0.08
total_years=20

year,total_asset=Compound_interst_calc(monthly_deposite,total_years,yearly_interest,plot=True)
'''

