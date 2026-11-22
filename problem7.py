primes = [2]
num = 3

while len(primes) < 10001:
    if num % 2 == 0:
        num += 1
        continue 

    is_prime = True
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            is_prime = False
            break  

    if is_prime:
        primes.append(num)
    
    num += 1

print(f"Found {len(primes)} primes. The 10,000th prime is {primes[-1]}.")
