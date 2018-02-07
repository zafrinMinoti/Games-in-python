from random import choice
import re


# Functions
def get_current_state(show_or_shy_dict):
	output_current_state = list()
	for k,v in show_or_shy_dict.items():
		if v == show:
			output_current_state.append(k)
		if v == shy:
			output_current_state.append('_')
	return output_current_state 

# create a dictionary
dictionary = ['computer', 'hardware', 'software', 'fusion', 'alpha', 'alphabet']

# Random word for hangman
word = choice(dictionary)

word = list(word)
print(word)

# Set initial shy(not show) values
show_or_shy = dict()
show = True; shy = False
for ltr in enumerate(word):
	show_or_shy[ltr] = shy

#print(current_state)
print(get_current_state(show_or_shy))
current_state = get_current_state(show_or_shy)
# Take user's input for letters
life = 3
while life >= 0:
	letter = input('Guess a letter: ')

	# check if all the letters are found
	if '_' not in current_state:
		print('You win!!!')
		break

	# Check if the letter user gussed is in the word
	elif letter in word:
		show_or_shy[letter] = show
		current_state = get_current_state(show_or_shy)
		print(current_state)

	# if the guess is wrong
	elif letter not in word:
		life -=1
		if life < 0:
			Print('Sorry! You lost! :(')

	# Take away life for wrong gusses
	else:
		print('Something else')
		
print