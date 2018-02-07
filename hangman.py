from random import choice

# Functions
def get_current_state(show_or_shy_dict):
	output_current_state = list()
	for k,v in show_or_shy_dict.items():
		if v == show:
			output_current_state.append(k[1])
		if v == shy:
			output_current_state.append('_')
	return output_current_state 

# create a dictionary
dictionary = ['computer', 'hardware', 'software', 'fusion', 'alpha', 'alphabet']

# Random word for hangman
word = list(choice(dictionary))

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
while life > 0:
	letter = input('Guess a letter: ')

	# Check if the letter user gussed is in the word
	if letter in word:
		for l in enumerate(word):
			if l[1] == letter:
				show_or_shy[l] = show
		current_state = get_current_state(show_or_shy)
		print(current_state)

		# check if all the letters are found
		if '_' not in current_state:
			print('You win!!!')
			break


	# if the guess is wrong
	elif letter not in word:
		life -=1
		print('That was a wrong guess.')
		print('Life left:', life)
		if life == 0:
			print('Sorry! You lost! :(')
			print('The word was', ''.join(word))
			break

	# Take away life for wrong gusses
	else:
		print('Something is wrong')
		
### Ways to improve
### Load an actual dictionary for feeding words
### do you want to play in again?

# add hint
# show vowels
# make diff levels of dificulity to choose at the beganning by choosing what mentioned above
