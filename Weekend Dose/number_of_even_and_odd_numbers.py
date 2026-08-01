""" Get the Number of even and odd number """


def number_of_even(numberIn):
	even_counter = 0
	
	for number in numberIn:
		if number % 2 == 0: 
			even_counter += 1

	return even_counter

def number_of_odd(numberIn):
	odd_counter = 0

	for number in numberIn:
		if number % 2 != 0: 
			odd_counter += 1

	return odd_counter


def number_of_even_odd(*number):
	all_numbers_inputed = list(number)

	even_numbers = str(number_of_even(all_numbers_inputed))
	odd_numbers = str(number_of_odd(all_numbers_inputed))

	return 'Odd Numbers: ' + odd_numbers + '\n' + 'Even Numbers: ' + even_numbers

print()

print(number_of_even_odd(3,4,5,6,7,8,5))