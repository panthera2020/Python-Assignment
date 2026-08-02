""" Factorial """

print('Get the factorial of the number')

user_number = int(input('Enter number: \n'))

factorial = 1

for numbers in range(user_number, 0, -1):
	factorial *= numbers

print()

print(user_number,'! = ', factorial)