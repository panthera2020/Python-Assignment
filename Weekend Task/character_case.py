""" Determine if the first character of a string is uppercase or lower case """

# Collect string input from user
# Isolate the first charcter 
# Check if character is a lowercase, Display lower case
# Check if charcater is uppercase, Display uppercase

word = input('Enter word: ')

print()

if word[0] == word.lower()[0]: print('First letter is Lowercase')

elif word[0] == word.upper()[0]: print('First letter is Uppercase')