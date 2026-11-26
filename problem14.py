results = []

for i in range(1, 1_000_000):
    n = i
    k = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        k += 1
    results.append(k)
    print(i, k)

print(results.index(max(results)) + 1)
