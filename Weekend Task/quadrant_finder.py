""" Quadrant Finder """

# Ask for two integers x and y
# if x > 0 and y > 0, Display Q1
# if x < 0 and y > 0, Display Q2
# if x < 0 and y < 0, Display Q3
# if x > 0 and y < 0, Display Q4
# if x and y equals to Zero, Display Origin
# if x!= 0 and y == 0, Display X-axis
# if x == 0 and y!= 0, Display Y-axis

print('Find the quadrant')

x = int(input('Enter first integer(x): '))

y = int(input('Enter second integer(y): '))

print()

if x > 0 and y > 0: print('Q1')
elif x < 0 and y > 0: print('Q2')
elif x < 0 and y < 0: print('Q3')
elif x > 0 and y > 0: print('Q4')
elif x == 0 and y == 0: print('Origin')
elif x != 0 and y == 0: print('X-axis')
elif x == 0 and y != 0: print('Y-axis')
