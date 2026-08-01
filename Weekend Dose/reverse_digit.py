""" Reverse the integer digits """

def reverse(numbers):
	individual_numbers = list(numbers)

	for _ in range(len(individual_numbers) -1, -1, -1):
		print(individual_numbers[_], end='')


user_integer = input('Enter Number: ')

print()

reverse(user_integer)