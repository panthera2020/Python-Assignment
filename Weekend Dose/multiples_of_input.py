""" Determine the multiple of a number from 1-100 """

def multiples(number):
	counter = 0

	for _ in range(1, 100):
		if number % _ == 0: counter += 1

	return counter

print("Get the multiples of your number")

print()

user_number = int(input('Enter Number: '))

print()

print('The are', multiples(user_number), 'multiples of',user_number, 'between 1-100')