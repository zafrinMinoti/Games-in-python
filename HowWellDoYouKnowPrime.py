from prime import isPrime
from time import monotonic, time
from random import randint

def show_number():
	return randint(1, 49)
def guess_match(input_yn):
	return True if input_yn == 'y' else False

start_time = monotonic()
end_time = start_time + 5

N = show_number()
prim = isPrime(N)
score = 0

while end_time > monotonic():
	print('\nNumber:', N)
	user_input = input('Is the number above prime?\n\
\ty = yes\n\tn = no\n\
You have 5 seconds... \nAnswer:\t')

	guess = guess_match(user_input)
	
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