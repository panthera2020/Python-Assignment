""" Get the Sum of number from 1 to Number inputed """

def sum_to_input(number):
	total = 0

	for _ in range(number,0,-1):
		total += _

	return total

print('Get the sum of your number from your input to 1')

print()

user_number = int(input('Enter Number:'))

print()

print('Answer: ', sum_to_input(user_number))