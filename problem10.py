# delt på to?
# anta at primtall
# if tall == j og j er sånn sqrt(i) eller noe
# nei glem det
# jo husk det

primes = [2,3,5,7]
n = 2_000_000

for i in range(11, n, 2):
  prime = True

  for j in range(3, int(i ** 0.5) + 1, 2):
    if i % j == 0:
      prime = False
      break
  
  if prime:
    primes.append(i)

print(sum(primes))