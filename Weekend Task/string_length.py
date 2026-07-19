""" Determine if a string input is a short string, medium string or Long string """

# Collect the user string input
# check if the string length is less than 5, Display short string
# Check if string lenght is between 5 and 10, Display medium string
# If string lenghth is above 10, display Long string

print('Get the lenght category of your input')\

word = input('Enter word: ')

print()

if len(word) < 5: print('Short String')

elif 5 <= len(word) <= 10: print('Medium String')

elif len(word) > 10: print('Long String')