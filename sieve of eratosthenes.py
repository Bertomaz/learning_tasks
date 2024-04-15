
primes = [2]
number = 3
while len(primes) < 100:
    is_prime = True
    for i in range(len(primes)):
        possible_prime = number // primes[i]
        if possible_prime * primes[i] == number:
            is_prime = False
    if is_prime:
        primes.append(number)

    
    number = number + 1
print(primes[99])
