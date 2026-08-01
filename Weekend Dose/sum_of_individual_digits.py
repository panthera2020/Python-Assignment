""" Get the sum of an individual digits of a number """

def sum_of_digits(user_input):
	total = 0

	for digits in user_input:
		total += int(digits)

	return total

print('Get the sum of individual digits in an integer')

print()

user_integer = input('Enter number: ')

print()

print('Sum of digits: ', sum_of_digits(user_integer))