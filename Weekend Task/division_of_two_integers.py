""" Divide two integers and don't do zero division """

# collect two integers x and y  
# calculate x divided by y is not equal to zero
# Display result
# if y is equals to zero 
# Display cannot divide by Zero

print('Input Two Integers(x,y)')

x = int(input('First integer(x): '))

y = int(input('Second integer(y): '))

print()

if y != 0: 
	result = x / y 
	print('x / y =', result)
if y == 0: print('Cannot divide by Zero')
