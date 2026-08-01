""" Calculate base raised to the power exponent """

def exponent_base(number):
	product = 1

	for _ in range(number):
		product *= number

	return product

user_number = int(input('Enter Number: '))

print()

print('Answer: ', exponent_base(user_number))

