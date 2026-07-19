""" determine if number is divisible by 5 and 3 """

# Collect number from user
# Check if number is divisble by 3 and 5, Display divisble by 5 and 3
# else, Display not divisible by 5 and 3

number = int(input('Enter number: '))

print()

if number % 5 == 0 and number % 3 == 0: print('Number is divisible by 5 and 3')

else: print('Number is not divisible by 5 and 3')