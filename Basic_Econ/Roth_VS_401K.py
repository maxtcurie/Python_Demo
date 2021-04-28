import numpy as np
import matplotlib.pyplot as plt

from Econ_tools import Compound_interst_calc


monthly_deposite=300.
yearly_interest=0.08
total_years=20

Salary_tax=0.50
Stock_tax =0.20

#for the case of 401K, no matching
year,total_asset,total_asset_after_tax=Compound_interst_calc(monthly_deposite,total_years,yearly_interest,tax_rate=Stock_tax,plot=False)
year_401K=year
total_asset_401K=total_asset_after_tax

#for the case of Roth IRA, no matching
year,total_asset,total_asset_after_tax=Compound_interst_calc(monthly_deposite*(1.-Salary_tax),total_years,yearly_interest,tax_rate=0,plot=False)
year_Roth=year
total_asset_Roth=total_asset_after_tax

plt.clf()
plt.plot(year_401K,total_asset_401K,label='401K')
plt.plot(year_Roth,total_asset_Roth,label='Roth IRA')
#plt.yscale("log")
plt.grid()
plt.legend()
plt.show()



Salary_tax_list=np.arange(0,0.7,0.01)
Stock_tax_list =np.arange(0,0.7,0.01)
plot_Salary_tax_list=Salary_tax_list
plot_Stock_tax_list=Stock_tax_list
plot_401_list=np.zeros((len(Salary_tax_list),len(Stock_tax_list)))
plot_Roth_list=np.zeros((len(Salary_tax_list),len(Stock_tax_list)))

for i in range(len(Salary_tax_list)):
	for j in range(len(Stock_tax_list)):
		Salary_tax=Salary_tax_list[i]
		Stock_tax=Stock_tax_list[j]
		#for the case of 401K, no matching
		year,total_asset=Compound_interst_calc(monthly_deposite,total_years,yearly_interest,plot=False)
		year_401K=year
		total_asset_401K=(total_asset-total_years*monthly_deposite*12.)*(1.-Stock_tax)+total_years*monthly_deposite*12.

		#for the case of Roth IRA, no matching
		year_Roth,total_asset_Roth=Compound_interst_calc(monthly_deposite*(1.-Salary_tax),total_years,yearly_interest,plot=False)

		plot_401_list[i,j]=total_asset_401K[-1]
		plot_Roth_list[i,j]=total_asset_Roth[-1]


percent_list=np.array(np.arange(0,1.,0.1)) #percents contribute to 401K
total_gain=np.zeros((len(Salary_tax_list),len(Stock_tax_list),len(percent_list)))

Max_gain_percent=np.zeros((len(Salary_tax_list),len(Stock_tax_list)))

for i in range(len(Salary_tax_list)):
	for j in range(len(Stock_tax_list)):
		for k in range(len(percent_list)):
			total_gain[i,j,k]=plot_401_list[i,j]*percent_list[k]+plot_Roth_list[i,j]*(1.-percent_list[k])
		Max_gain_percent[i,j]=percent_list[np.argmax(total_gain[i,j,:])]


fig, ax=plt.subplots(nrows=3,ncols=1,sharex=True,sharey=True) 
ax[0].contourf(plot_Salary_tax_list,plot_Stock_tax_list,plot_401_list,levels=1000)
ax[0].set_title('401K final')

ax[1].contourf(plot_Salary_tax_list,plot_Stock_tax_list,plot_Roth_list,levels=1000)
ax[1].set_title('Roth final')

ax[2].contourf(plot_Salary_tax_list,plot_Stock_tax_list,Max_gain_percent,levels=1000)
ax[2].set_title('Percent to 401K for maximum return')
ax[2].set_xlabel('Salary tax')
ax[2].set_ylabel('Stock tax')

plt.tight_layout()
plt.show()

plt.clf()
plt.contourf(plot_Salary_tax_list,plot_Stock_tax_list,Max_gain_percent,levels=1000)
plt.title('Percent to 401K for maximum return')
plt.xlabel('Salary tax')
plt.ylabel('Stock tax')
plt.colorbar()
plt.show()