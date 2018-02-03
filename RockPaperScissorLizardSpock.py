# Imports
import random

available_choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

while True:
	while True:
		# players choice
		player_choice = input("Choose one:\nRock, Paper, Scissors, Lizard or Spock? ").lower()

		# computer's choice
		comp_choice = random.choice(available_choices)

		# Validation loop for ties
		if player_choice == comp_choice:
			print('Oops... that\'s a tie\nPlease try again\n')
			continue

		# Validation loop for invalid choices
		if player_choice not in available_choices:
			print('Oops... that\'s an invalid choice.\n')
			continue

		break

	# Determine Winner
	players = ['Player', 'Computer']
	actual_choices = [player_choice, comp_choice]

	def default():
		default_winner = 'Not Determined'
		return(default_winner)

	for plr, choice in enumerate(actual_choices):
		if 'rock' in actual_choices:
			if 'paper' in actual_choices or 'spock' in actual_choices:
				if choice == 'paper' or choice == 'spock':
					winner = plr
					statement = 'Paper covers rock\nand Spock vaporizes rock.'
			elif 'scissors' in actual_choices or 'lizard' in actual_choices:
				if choice == 'rock':
					winner = plr
					statement = 'Rock crushes Scissors\nand Rock crushes Lizard'
			else:
				winner = default()

		elif 'paper' in actual_choices:
			if 'spock' in actual_choices:
				if choice == 'paper':
					winner = plr
					statement = 'Paper disproves Spock'
			elif 'scissors' in actual_choices or 'lizard' in actual_choices:
				if choice == 'scissors' or choice == 'lizard':
						winner = plr
						statement = 'Scissors cuts Paper\nand Lizard eats Paper'
			else:
				winner = default()

		elif 'scissors' in actual_choices:
			if 'spock' in actual_choices:
				if choice == 'spock': 
					winner = plr
					statement = 'Spock smashes Scissors'
			elif 'lizard' in actual_choices:
				if choice == 'Scissors':
					winner = plr
					statement = 'Scissors decapitates Lizard'
			else:
				winner = default()

		if 'lizard' in actual_choices:
			if 'spock' in actual_choices:
				if choice == 'lizard':
					winner = plr
					statement = 'Lizard poisons Spock'
			else:
				winner = default()

	# Convert winner number to winner name
	try: 
		winner = players[winner]
	except: 
		pass

	# Print
	print()
	print('Computer: ', comp_choice)
	print('Your choice: ', player_choice)
	print()
	print('The winner is: ', winner)
	if winner == default():
		print(player_choice, 'and', comp_choice,
			'does not bit one another',
			'\nPlease Try again...\n')
	else:
		print('Because,', statement)
		break
		