""" Find the two largest Value """

print('Determine the two largest values')
number = int(input('Enter numbers: \n'))

largest = number
second_largest = 0;

for numbers in range(9):
	number = int(input())

	if number > largest:
		second_largest = largest
		largest = number
	elif number > second_largest and number < largest: second_largest = number

print('Largest: ', largest)
print('Second Largest: ', second_largest)
