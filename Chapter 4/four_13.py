
def product(*numbers):
	product = 1

	for number in numbers:
		product *= number

	return product

print(product(1,2,4,5,6,7))

print()

print(product(3,3,3))

print()

print(product(5,4,2,2))