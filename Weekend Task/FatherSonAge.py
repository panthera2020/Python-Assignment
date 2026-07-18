""" Calculate how many years ago father was twice as old as son """

# Question 1
# collect Fathers age
# collect sons age
# Calculate how many years ago father was twice son's age, 2(son age) - fatherage
# Display result

father_age = int(input('Enter Father Age: '))

son_age = int(input('Enter Son age: '))

if 0 < father_age <= 80 and 0 < son_age <= 80:
	years = (2 * son_age) - father_age

	if years < 0: print('Father was twice son age ', -years, 'years ago')
	else: print('Father was twice son age ', years, 'years ago')

else: print('Invalid Input!!!')