import random

def question():
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

question()