import numpy as np 
import pandas as pd
import csv


#!!!!!!!!!!!!!!!!Need to and consider A as 1 or 11 functionility 
csvfile_name="Blackjack_log.csv"
name_list=['0','1','2','3','4','5','6','7','8','9','10']

Deck_num=2	#number of the decks of cards


card_list_fresh=[Deck_num*4]*11
card_list_fresh[-1]=Deck_num*4*4  #10 has 10/J/Q/K

def calc_card(): #Calculate the expected value from 1-K
	data_cards=pd.read_csv(csvfile_name)
	used_card_list=[0]*11
	for i in name_list:
		used_card_list[int(i)]=np.sum(data_cards[i])
	card_list=np.array(card_list_fresh)-np.array(used_card_list)
	print("reminding playing cards: "+str(card_list))
	n_tot=np.sum(card_list)
	odd_value=card_list/n_tot
	Exp_value=np.sum(np.arange(11)*card_list/n_tot)
	return Exp_value, odd_value, card_list #Expected value for value of 1-K, odd of getting A

'''
test_list=[2,4,3,4,2,4,1,1,2,0,1]
print(type(test_list))
test_list=np.array(test_list)
print(len(test_list))
print(calc_card(test_list))
'''

def hit_or_nah(odd_value,house_total,player_total):
	hit_or_nah_output=0
	print('House odd')
	house_card_list=house_total+np.arange(11)
	if house_total+11<=21:
		house_card_list[0]=house_total+11
	else: 
		house_card_list[0]=house_total+1
	print(str(house_card_list))
	print(str(odd_value*100))

	print('Player odd')
	player_card_list=player_total+np.arange(11)
	if player_total+11<=21:
		player_card_list[0]=player_total+11
	else:
		player_card_list[0]=player_total+1
	print(str(player_card_list))
	print(str(odd_value*100))
	hit_odd=0.
	for i in range(11):
		if player_card_list[i]<=21:
			hit_odd=hit_odd+odd_value[i]
	if hit_odd>0.5:
		hit_or_nah_output=1
	return hit_or_nah_output,hit_odd

def card_update(house_card,player_card):
	house_card_temp=[0]*11
	player_card_temp=[0]*11
	with open(csvfile_name, 'a+', newline='') as csvfile:
		data = csv.writer(csvfile, delimiter=',')
		card_info=[0]*11
		if house_card>=0:
			card_info[house_card]=card_info[house_card]+1
			house_card_temp[house_card]=house_card_temp[house_card]+1
		if player_card>=0:
			card_info[player_card]=card_info[player_card]+1
			player_card_temp[player_card]=player_card_temp[player_card]+1
		print('player card list: '+str(player_card_temp))
		print('hosue card list: '+str(house_card_temp))
		data.writerow(card_info)
		csvfile.close()

def main_function():	
	with open(csvfile_name, 'w', newline='') as csvfile:
		data = csv.writer(csvfile, delimiter=',')
		data.writerow(['0','1','2','3','4','5','6','7','8','9','10'])
		csvfile.close()
	
	input_temp=1
	while(input_temp!=0):
		input_temp=int(input("Keep playing? (0. no, 1. yes): "))
		house_total=0
		player_total=0
		
		
			
		#*****Beginning section***************
		house_card=int(input("House card(-1-10): "))	#0 for A, 10 for 10/J/Q/K, -1 for stand
		player_card=int(input("Player card(-1-10): "))
		player_card2=int(input("Player card2(-1-10): "))
		if house_card==0:
			house_card=1	
		if player_card==0:
			player_card=1
		if player_card2==0:
			player_card2=1
		if player_card==0 and player_card2==0:
			player_card=11
			player_card2=1

		house_total=house_total+house_card
		player_total=player_total+player_card+player_card2

		card_update(house_card,player_card)
		card_update(-1		  ,player_card)
			
		Exp_value, odd_value, card_list=calc_card()
		#print('Exp_value='+str(Exp_value))
		#print('odd_value='+str(odd_value))

		#**********player hit
		hit=1
		print("player hit")
		while(hit==1):
			output_temp,odd_temp= hit_or_nah(odd_value,house_total,player_total)
			print('odd: '+str(odd_temp))
			if output_temp==1:
				print("HIT!")
			else: 
				print("Stand!")
			hit=int(input('hit? 0. no 1. yes'))
			if hit==1:
				player_card=int(input("Player card(-1-10): "))
				card_update(-1		  ,player_card)
				player_total=player_total+player_card
				Exp_value, odd_value, card_list=calc_card()

		#*************house hit
		
		print("house hit")
		while(house_card<12):
			house_card=int(input("House card(-1-10): "))
			if house_card>=12:
				break
			card_update(house_card,-1)
			




main_function()
