""" Guessing the Random Number """

import random

number = 0

for numbers in range(1, 1000):
	number = random.randrange(numbers)

print('Guess my number between 1 and 1000 with the fewest guess')

while True:
	user_number = int(input('Enter number (-1 to quit): '))

	if(user_number == -1): break

	elif(user_number > number): print('Too high. Try again')

	elif(user_number < number): print('Too Low. Try again')

	elif(user_number == number): 
		print('Congratulations. You guessed the number!')

		print()

		print('Do you want to play again?')
		user_input = input('Yes or No\n')

		if(user_input.lower() == 'no'): break

		elif(user_input.lower() == 'yes'):
			print('\nNew game started \nGuess my number between 1 and 1000 with the fewest guess')
			
			for numbers in range(1, 1000):
				number = random.randrange(numbers)
	