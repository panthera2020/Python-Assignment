""" Miles per Gallon """

gallons = float(input('Enter the gallons used (-1 to end):'))

miles = float(input('Enter the miles driven: '))

miles_per_gallon = miles / gallons

print('The miles/gallon for this tank was', miles_per_gallon)

add = 0
counter = 1

while(gallons != -1):
	add += miles_per_gallon

	counter += 1

	gallons = float(input('Enter the gallons used (-1 to end):'))

	miles = float(input('Enter the miles driven: '))

	miles_per_gallon = miles / gallons

	print('The miles/gallon for this tank was', miles_per_gallon)


average = add / counter

print('The overall average miles/gallon was ', average)