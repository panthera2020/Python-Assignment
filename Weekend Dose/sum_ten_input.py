""" Sum ten number numbers """

print('Enter 10 numbers and get the sum')

print()

total = 0

for _ in range(10):
	user_number = int(input('Enter number:'))
	total += user_number

print()

print('The sum: ', total)