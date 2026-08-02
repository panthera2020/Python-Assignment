""" Separating the digits in an Integer """

user_number = int(input('Enter 5 digit integer: \n'))

for numbers in range(5):
	digit = user_number % 10
	print(digit, end=' ')
	user_number = user_number // 10
