import csv



with open('RIP_ratio.csv', 'w') as csvfile:		#clear all and then write a row
    RIP_data = csv.writer(csvfile, delimiter=',')
    RIP_data.writerow(['Z(m)','Ratio','integrate_B1_n0_dR','integrate_n0_dR','n0_BES','n1_BES','B0_BES'])
csvfile.close()

with open('RIP_ratio.csv', 'a+') as csvfile:	#adding a row
    RIP_data = csv.writer(csvfile, delimiter=',')
    RIP_data.writerow(['Z(m)','Ratio','integrate_B1_n0_dR','integrate_n0_dR','n0_BES','n1_BES','B0_BES'])
csvfile.close()