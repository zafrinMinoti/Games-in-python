'''
This program shows random numbers to the user.
The user have 5 seconds to guess if the number is prime.
The program validate user's mput and gives score.
'''

from prime import isPrime
from time import monotonic, time
from random import randint

# Functions
def show_number():
	return randint(1, 4242)

def guess_match(input_yn):
	if input_yn == 'y':
		return True
	if input_yn == 'n':
		return False

def game_duration():
	print('This game is called "How well do you know your primes?"')
	time = int(input('How long (in seconds) would you like to play this game?'))
	return time

# Let's play
DURATION = game_duration()

start_time = monotonic()
end_time = start_time + DURATION

score = 0
cycle = 0

user_input = None
while end_time > monotonic():
	N = show_number()
	prim = isPrime(N)
	print('\nNumber:', N)

	user_input = input('Is the number above prime?\n\
You have 5 seconds... \n\ty = yes\n\tn = no\nAnswer: ')

	guess = guess_match(user_input)

	if guess is None: 
		print('INVALID INPUT')
		break
	
	if guess == prim and monotonic() < end_time:
		print('\nYou gussed right!')
		score += 1
		#break
	if guess != prim and monotonic() < end_time:
		print('\nIt was a wrong guess')
		score += 0
		#break
	if monotonic() > end_time:
		print('\nSorry, Time\'s up!')
		score += 0
		cycle += 1
		break
	else:
		cycle += 1
		continue

print('Score: {} out of {}'.format(score, cycle))
