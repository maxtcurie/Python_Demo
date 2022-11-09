import numpy as np 

card_list=np.arange(1,13,1,dtype=int)
print(card_list)
#choose=[]
total_score=0
for i in range(5):
    choose_tmp=np.random.choice(card_list)
    print(total_score)
    if choose_tmp==1:
        total_score=total_score*5
    elif 11<=choose_tmp or choose_tmp<=13:
        total_score=0
        break
    else:
        total_score=total_score+choose_tmp
    print(np.argmin(abs(card_list-choose_tmp))
    #card_list.pop(np.argmin(abs(card_list-choose_tmp))
        
#print(total_score)