""" Prime number checker """
def isprime(number):
	prime_counter = 0;

	is_number_prime = True

	for count in range(1,number + 1):
		if number % count == 0: 
			prime_counter += 1

	if prime_counter == 2: is_number_prime = True
	elif  prime_counter != 2: is_number_prime = False

	return is_number_prime 


def print_primes(number):
	number_prime = isprime(number)
	prime_counter = 0

	if number_prime == True:
		for  value in range(2, number):
			prime_counter = 0
			for values in range(1, number):
				if value % values == 0: 
					prime_counter += 1
			if prime_counter == 2:
				print(value, end=' ')
	elif number_prime == False: print('Number is not a prime')

print('Get the prime numbers between 1 and any prime number')

print()

user_number = int(input('Enter Number: '))

print()

print_primes(user_number)

