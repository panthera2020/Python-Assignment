""" Determine if letter is a vowel or consonant """

# Ask user for one letter
# if the input is either, a, e, i, o, u, Display vowel
# if not, Display consonant

print('Vowel or Consonant')

print()

print('Input one letter')

letter = input('Enter letter: ')

print()

if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u': print('Vowel')
else: print('Consonant')
