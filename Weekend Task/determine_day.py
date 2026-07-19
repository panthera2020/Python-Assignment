""" Determine the day of the week """

# collect input between 1 - 7 
# if 1, Display Sunday
# if 2, display Monday
# if 3, Display Tuesday
# if 4, Display Wednesday
# if 5, Display Thursday
# if 6, Display Friday 
# if 7, Display Saturday 

print('Determine the day of the week')
day = int(input('Enter Number: '))

if 1 <= day <= 7:
	match day:
		case 1: print('Sunday')
		case 2: print('Monday')
		case 3: print('Tuesday')
		case 4: print('Wednesday')
		case 5: print('Thursday')
		case 6: print('Friday')
		case 7: print('Saturday')
else: print('Invalid input')