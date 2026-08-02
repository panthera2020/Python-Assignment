""" Arimetic, Smallesr and Largest"""

print('Get the sum, average, product, smallest and largest of four numbers')
print()
number = int(input('Enter numbers:\n'))
add = 0
product = 1
largest = number
smallest = number

for numbers in range(3):
	add += number
	product *= number
	number = int(input())
	if number > largest: largest = number
	elif number < smallest: smallest = number

average = add / 4

print()

print('Sum: ', add)
print('Average: ', average)
print('Product: ', product)
print('Smallest: ', smallest)
print('Largest: ', largest)