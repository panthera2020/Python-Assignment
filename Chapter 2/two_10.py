""" Determine the sum average, product, smallest and largest of the number """

# Collect three integers seperately
# Determine the smallest and largest number using min and max function
# Add all the numbers to get the sum
# Divide the sum by 3 to get the average
# Mulitply the three numbers to get the product
# Display sum average, product, smallest and largest 

first_number = int(input('Enter first number: '))

second_number = int(input('Enter second number: '))

third_number = int(input('Enter third number: '))

min (first_number, second_number, third_number)

max (first_number, second_number, third_number)

numbers = (first_number, second_number, third_number)

average = (sum(numbers)) / 3

product = first_number * second_number * third_number

print('Sum: ', sum(numbers))

print('Average: ', average)

print('Product: ', product)

print('Largest Number: ', max(first_number, second_number, third_number))

print('Smallest Number: ', min(first_number, second_number, third_number))