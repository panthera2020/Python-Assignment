""" Print a mulitiplication table of the input fro  1-10 """

def multiplication_table(number):
	for _ in range(1,11):
		print(f'{number} * {_:>2} = {number * _: >3}') 

print('Get the Multiplication from 1-10')

print()

user_number = int(input('Enter Number:'))

print()

multiplication_table(user_number)