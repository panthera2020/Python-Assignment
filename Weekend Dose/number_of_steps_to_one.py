
def number_of_steps_to_one(number):

	counter = 0

	while True:
		if number <= 1: break

		elif number % 2 == 0: 
			answer = number / 2
			number = answer
			counter += 1 
			
		elif number % 2 != 0: 
			answer = number * 3 + 1
			number = answer
			counter += 1

	return counter

print('Get the number of steps that get the number to one')

print()

user_number = int(input('Enter positive number: '))

print()

print('The number of steps to one is', number_of_steps_to_one(user_number))