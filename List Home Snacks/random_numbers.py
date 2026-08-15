import random 

numbers = []

for _ in range(10):

	random_number = random.randrange(1,50)

	numbers.append(random_number)

for number in numbers:
	print(number, " ", end=" ")