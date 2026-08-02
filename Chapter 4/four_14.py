import random

def question():
	firstNumber = random.randrange(1,10)

	secondNumber = random.randrange(1,10)

	answer = firstNumber * secondNumber

	while True:
		print('What is', firstNumber, '*', secondNumber, '?')
		user_answer = int(input())

		print()

		if answer == user_answer:
			print('Very Good')
			break
		elif answer != user_answer:
			print('No. Please try again.')

question()