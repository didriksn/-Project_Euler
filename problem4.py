a = 999
b = 999

all = []

for i in range(999*999):
  if str(a*b)[::-1] == str(a*b):
    all.append(a*b)

  b -= 1

  if b == 100:
    a -= 1
    b = 999

print(max(all))