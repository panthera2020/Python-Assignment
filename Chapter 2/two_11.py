""" Seperating the Digits in an Integers """

# Collect a five digit integer 
# if the number is not a five digit, print invalid input
# Use floor division from 10000, then by 1000, then 100, then 10
# use modulo to pick off each of the number
# print each of the number with a space

number_input = int(input('Enter a five digit integer: '))

if 10001 <= number_input <= 99999: 
	first_digit = number_input // 10000

	second_digit = (number_input // 1000) % 10

	third_digit = (number_input // 100) % 10

	fourth_digit = (number_input // 10) % 10

	fifth_digit = number_input % 10

	print(first_digit,'\t', second_digit, '\t', third_digit, '\t', fourth_digit, '\t', fifth_digit)

else: print('Invalid input')