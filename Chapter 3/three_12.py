""" Palindromes """

print('Determine is the number is a palindrome')

print()

number = int(input('Enter five digit integer \n'))

first_digit = (number // 10000) % 10

second_digit = (number // 1000) % 10

fourth_digit = (number // 10) % 10

fifth_digit = number % 10 

print()

if first_digit == fifth_digit and second_digit == fourth_digit: print('PALINDROME')

else: print('Not PALINDROME')