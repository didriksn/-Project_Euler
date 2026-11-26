import math

i = 2000


while True:
    x = 0
    k = 0
    for j in range(1, i):
        k += j

    for l in range(1, math.floor(math.sqrt(k))):
        if k % l == 0:
            x += 2

    print(k, x)

    if x > 500:
        print(k)
        break

    i += 1