fib = [1,2]
all = 0

while True:
  if fib[-1] + fib[-2] > 4000000:
    break
  else:
    fib.append(fib[-1] + fib[-2])

for i in fib:
  if i % 2 == 0:
    all += i

print(all)