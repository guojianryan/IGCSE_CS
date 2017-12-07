from random import randrange

options = ["rock","scissors","paper"]
computer_wins = 0
player_wins = 0
counter = 0

while counter < 5:
	#computer's choice
	computer_choice = randrange(len(options))

	#player's choice
	player_choice = -1
	while player_choice not in range(3):
		player_choice = int(input("Please enter your choice [0: rock, 1: scissors, 2:paper]"))

	print("Player vs Computer: {0}: {1} ".format(options[player_choice],options[computer_choice]))

	#if it is not a tie
	if computer_choice != player_choice:
		counter = counter + 1
		#the computer wins
		if computer_choice - player_choice == -1 or computer_choice - player_choice == 2:
			computer_wins = computer_wins + 1
		else:
			player_wins = player_wins + 1

	print("Player vs Computer: {0}: {1} ".format(player_wins,computer_wins))
	#end the game
	if player_wins == 3 or computer_wins == 3:
		break

    
