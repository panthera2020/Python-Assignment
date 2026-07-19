""" Determine if a character is a digit a letter or a special symbol """

# collect a single character from user
# check if the type is a string, Display String
# if integer Display integer
# if special charcater, Display special charcater

char = input('Enter character: ')

print()

if len(char) == 1:
	if char.isalpha(): print('Character is an alphabet')
	elif char.isdigit(): print('Character is a digit')
	else: print('Character is a special character')

else: print('Invalid Character')