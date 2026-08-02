import random

def question(number):
	if number == 1:

		firstNumber = random.randrange(1,10)

		secondNumber = random.randrange(1,10)

		answer = firstNumber * secondNumber

		

		one = 'Very Good!'
		two = 'Nice Work!'
		three = 'Good Work!'

		one_ = 'No. Please try again'
		two_ = 'Wrong. Try once more'
		three_ = 'No. Keep trying'

		while True:
			print('What is', firstNumber, '*', secondNumber, '?')
			user_answer = int(input())

			randomNumber = random.randrange(1,3)

			print()

			if answer == user_answer:
				if randomNumber == 1: print(one)
				elif randomNumber == 2: print(two)
				elif randomNumber == 3: print(three)
				break
			elif answer != user_answer:
				if randomNumber == 1: print(one_)
				elif randomNumber == 2: print(two_)
				elif randomNumber == 3: print(three_)

	elif number == 2:	
		firstNumber = random.randrange(1,99)

		secondNumber = random.randrange(1,99)

		answer = firstNumber * secondNumber

		

		one = 'Very Good!'
		two = 'Nice Work!'
		three = 'Good Work!'

		one_ = 'No. Please try again'
		two_ = 'Wrong. Try once more'
		three_ = 'No. Keep trying'

		while True:
			print('What is', firstNumber, '*', secondNumber, '?')
			user_answer = int(input())

			randomNumber = random.randrange(1,3)

			print()

			if answer == user_answer:
				if randomNumber == 1: print(one)
				elif randomNumber == 2: print(two)
				elif randomNumber == 3: print(three)
				break
			elif answer != user_answer:
				if randomNumber == 1: print(one_)
				elif randomNumber == 2: print(two_)
				elif randomNumber == 3: print(three_)


user_difficulty_level = int(input('Enter your difficulty level(1 or 2): \n'))

print()

if user_difficulty_level == 1 or user_difficulty_level == 2: question(user_difficulty_level)
else: print('Invalid Input')