""" Sort in Asending order """

# Collect three various floating points numbers from the user
# Check if the first number is the smallest, print it first
# Comapare the remaining two which is smaller, print that and the largest
# Check if the second number is the smallest, print it first
# Comapare the remaining two which is smaller, print that and the largest
# Check if the third number is the smallest, print it first
# Comapare the remaining two which is smaller, print that and the largest

print('Enter three floating point numbers')

first_number = float(input('Enter first number: '))

second_number = float(input('Enter second number: '))

third_number = float(input('Enter third number: '))

if first_number < second_number and first_number < third_number:
	print(first_number, end=" ")

	if second_number < third_number: print(second_number, third_number)
	else: print(third_number, second_number)

elif second_number < first_number and second_number < third_number:
	print(second_number, end =" ")

	if first_number <third_number: print(first_number, third_number)
	else: print(third_number, first_number)

elif third_number < first_number and third_number < second_number:
	print(third_number, end=" ")

	if first_number < second_number: print(first_number, second_number)
	else: print(second_number, first_number)

