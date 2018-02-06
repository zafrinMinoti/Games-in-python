def isPrime(num):
	prime = False

	if num == 2:
		prime = True
	elif num > 2:
		if num % 2 == 0:
			prime = False
	#first_primes = [3, 5, 7, 11]
		else:
			for n in range(3,num,2):
				if num % n == 0:
					prime = False
					break
	else:
		prime = True
	return prime

print(isPrime(int(input('Number? '))))

# 