from Math import sqrt, ceil

def isPrime(num):
    prime = False
    num_sqrt = ceil(sqrt(num))

    if num == 2:
        prime = True
    elif num > 2:
        if num % 2 == 0:
            prime = False

        elif num > 8:
            for n in range(3,num_sqrt+1,2):
                if num % n == 0:
                    prime = False
                    break
                else:
                    prime = True
        else:
            prime = True
    return prime