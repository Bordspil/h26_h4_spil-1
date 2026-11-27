import random
player1=0
player2=1
turn=0
player_value_1=0
player_value_2=0
counter_neg=4
counter_pos=1
bombs_neg_list=[]
bombs_pos_list
while counter_neg !=0:
    bombs_neg=random.randint(1,5)
    bombs_neg_list.append(bombs_neg)
    counter_neg-=1
    if turn==player1:
        player_value_1+=spaces
        turn+=1
    elif turn==player2:
        player_value_2+=spaces
        turn-=1
    
while counter_pos !=0:
        bombs_pos=random.randint(0,5)
    bombs_pos_list.append(bombs_neg)
    counter_pos-=1
    if turn==player1:
        player_value_1+=spaces
        turn+=1
    elif turn==player2:
        player_value_2+=spaces
        turn-=1
    
