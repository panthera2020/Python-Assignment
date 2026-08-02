""" Triangle Printing """

for numbers in range(10):
	for number in range(-1,numbers):
		print("*", end='')
	print()

print()

for numbers in range(10):
	for number in range(10,numbers, -1):
		print("*", end='')
	print()

print()

for numbers in range(10):
	for number in range(numbers):
		print(" ", end='')

	for number in range(10,numbers, -1):
		print("*", end='')

	print()

print()

for numbers in range(10):
	for number in range(10,numbers, -1):
		print(" ", end='')

	for number in range(-1, numbers):
		print("*", end='')

	print()