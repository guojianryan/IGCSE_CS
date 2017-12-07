import random

def one_round():
    doors = [1,1,0] # 1==goat, 0=car
    random.shuffle(doors) # shuffle doors
    choice = random.randint(0,2) 
    return doors[choice] 
    #If a goat is chosen, it means the player loses if he/she does not change.
    #This method returns if the player wins or loses if he/she changes. win = 1, lose = 0

def hall():
    change_wins = 0
    N = 10000
    for index in range(0,N):
        change_wins +=  one_round()
    print change_wins

hall()