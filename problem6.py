squareofsum = 0
sumofsquare = 0

for i in range(1, 101):
  sumofsquare += i**2
  squareofsum += i

squareofsum = squareofsum ** 2

print(abs(squareofsum - sumofsquare))