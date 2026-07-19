""" Determine if a three letter word is a palindrome """

# Collect string input from user
# if word lenght exceed three, Display invalid input
# if word lenght doesn't, Check if first character and last character are same
# If they are the same, Display Palindrome
# if not, Display not a Palindrome

print('Check if the three letter word is a PALINDROME')

word = input('Enter three letter word: ')

print()

if len(word) == 3:
	if word.lower()[0] == word.lower()[2]: print('PALINDROME')
	else: print('Not a PALINDROME')

else: print('Invalid input') 