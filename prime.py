from Math import sqrt

def isPrime(num):
	prime = False
	midpoint = num//2

	if num == 2:
		prime = True
	elif num > 2:
		if num % 2 == 0:
			prime = False
			
		elif num > 8:
			for n in range(3,midpoint,2):
				if num % n == 0:
					prime = False
					break
	else:
		prime = True
	return prime