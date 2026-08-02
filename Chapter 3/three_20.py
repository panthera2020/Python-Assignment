""" Binary to decimal Conversion """ 

print('Convert binary integers to decimal')

binary = int(input('Enter binary digits: \n'))

digit = 1
digit_counter = 0

while(digit != 0):
	digit = binary / 10
	digit_counter += 1

print(digit_counter)