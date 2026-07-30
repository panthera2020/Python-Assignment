""" Determine if the number is a PALINDROME or prime """

def whatis(numbers):

	prime_counter = 0;

	for count in range(1,numbers + 1):
		if numbers % count == 0: prime_counter += 1

	number = str(numbers)

	digits = list(number)

	is_palindrome = True

	for digit in range(0,len(digits)):
		if digits[digit] == digits[len(digits) - (1 + digit)]: 
			is_palindrome = True

		else: 
			is_palindrome = False
			break

	if prime_counter == 2 and is_palindrome == True: return 'is a Palindrome and a Prime Number'

	else: return 'is not a Palindrome and a Prime Number'
