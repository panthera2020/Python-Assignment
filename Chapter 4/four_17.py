import random

def multiply_question():
	firstNumber = random.randrange(1,11)

	secondNumber = random.randrange(1,11)

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

		randomNumber = random.randrange(1,4)

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

def add_question():
	firstNumber = random.randrange(1,11)

	secondNumber = random.randrange(1,11)

	answer = firstNumber + secondNumber

	

	one = 'Very Good!'
	two = 'Nice Work!'
	three = 'Good Work!'

	one_ = 'No. Please try again'
	two_ = 'Wrong. Try once more'
	three_ = 'No. Keep trying'

	while True:
		print('What is', firstNumber, '+', secondNumber, '?')
		user_answer = int(input())

		randomNumber = random.randrange(1,4)

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

def substract_question():
	firstNumber = random.randrange(1,11)

	secondNumber = random.randrange(1,11)

	answer = firstNumber - secondNumber

	

	one = 'Very Good!'
	two = 'Nice Work!'
	three = 'Good Work!'

	one_ = 'No. Please try again'
	two_ = 'Wrong. Try once more'
	three_ = 'No. Keep trying'

	while True:
		print('What is', firstNumber, '-', secondNumber, '?')
		user_answer = int(input())

		randomNumber = random.randrange(1,4)

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

def divide_question():
	firstNumber = 1
	secondNumber = 2

	while secondNumber > firstNumber:
		firstNumber = random.randrange(1,11)

		secondNumber = random.randrange(1,11)


	answer = round(firstNumber / secondNumber, 2)

	

	one = 'Very Good!'
	two = 'Nice Work!'
	three = 'Good Work!'

	one_ = 'No. Please try again'
	two_ = 'Wrong. Try once more'
	three_ = 'No. Keep trying'

	while True:
		print('What is', firstNumber, '/', secondNumber, '?')
		user_answer = round(float(input()), 2)

		randomNumber = random.randrange(1,4)

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

def question_type(number):
	if number == 1: add_question()
	elif number == 2: substract_question()
	elif number == 3: multiply_question()
	elif number == 4: divide_question()
	elif number == 5: 
		get_random_number = randrange(1,4)
		if get_random_number == 1: add_question()
		elif get_random_number == 2: substract_question()
		elif get_random_number == 3: multiply_question()
		elif get_random_number == 4: divide_question()


print()

while True:
	user_input = int(input("""

Pick an arithmetic problem to study

For Addition Problems -> Enter 1
For Substraction Problems -> Enter 2
For Multiplication Problems -> Enter 3
For Division Problems -> Enter 4
For Random Problem -> Enter 5 

To Quit -> Enter 0

		"""))

	if user_input == 0: break

	question_type(user_input)

