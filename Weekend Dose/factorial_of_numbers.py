""" Determine the factorial of a given number """

def factorial(number):
	product = 1

	for _ in range(number, 0, -1):
		product *= _ 

	return product

print('Get the factorial of the number')

print()

user_number = int(input('Enter Number:'))

print()

print('Answer: ', factorial(user_number))