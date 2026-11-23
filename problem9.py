import math

a = 500
b = 500

triplets = []

for i in range(0, 500*500):
  if math.sqrt(a**2 + b**2) == math.floor(math.sqrt(a**2 + b**2)):
    # triplets.append(f"a: {a} b: {b} c: {int(math.sqrt(a**2 + b**2))}")
    if a + b + math.sqrt(a**2 + b**2) == 1000:
      print(f"a:{a} b:{b} c:{math.sqrt(a**2 + b**2)}")

  if b == 1:
    b = 500
    a -= 1
    continue
  b -= 1

print(200 * 375 * 425)