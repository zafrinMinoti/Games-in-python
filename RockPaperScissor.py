# Imports
import random

available_choices = ['rock', 'paper', 'scissors']

while True:
	# players choice
	player_choice = input("Choose one: Rock, Paper or Scissors? ").lower()

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

for plr, choice in enumerate(actual_choices):
	if 'rock' in actual_choices:
		if choice == 'paper':
			winner = plr
			statement = 'Paper wraps rock'
		elif choice == 'rock':
			winner = plr
			statement = 'Rock smashes scissors'
	elif 'rock' not in actual_choices:
		if choice == 'scissors':
			winner = plr
			statement = 'Scissors cut paper'

# Convert winner number to winner name
winner = players[winner]

# Print
print()
print('Computer: ', comp_choice)
print('Your choice: ', player_choice)
print()
print('The winner is: ', winner)
print('Because,', statement)