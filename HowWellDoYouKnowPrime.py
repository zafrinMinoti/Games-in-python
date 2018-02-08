from prime import isPrime
from time import monotonic, time
from random import randint

def show_number():
	return randint(1, 4242)

def guess_match(input_yn):
	if input_yn == 'y':
		return True
	elif input_yn == 'n':
		return False
	else:
		print('INVALID INPUT')

start_time = monotonic()
end_time = start_time + 5

N = show_number()
prim = isPrime(N)
score = 0

user_input = None
while end_time > monotonic():
	print('\nNumber:', N)

	try:
		if user_input is None or user_input != 'y' or user_input != 'n':
			user_input = input('Is the number above prime?\n\
\ty = yes\n\tn = no\n\
You have 5 seconds... \nAnswer:\t')
			guess = guess_match(user_input)

	except: 
		continue
		break
	
	if guess == prim and monotonic() < end_time:
		print('\nYou gussed right!')
		score += 1
		break
	if guess != prim and monotonic() < end_time:
		print('\nIt was a wrong guess')
		score = 0
		break
	if monotonic() > end_time:
		print('\nSorry, you were too late!')
		score = 0
		break

print('Score:', score)