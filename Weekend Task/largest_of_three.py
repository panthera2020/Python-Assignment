""" Largest of three """

# Collect three input a, b, c
# Make the first number the largest 
# compare the other input to the remaining number to determine the largest
# Print largest

print('Largest of three integers')

first_integer = int(input('Enter first integer: '))

second_integer = int(input('Enter second integer: '))

third_integer = int(input('Enter third integer: '))

largest = first_integer

if second_integer > largest and second_integer > third_integer: largest = second_integer
if third_integer > largest and third_integer > second_integer: largest = third_integer

print()
print('Largest Integer is ',largest)