""" Ticket Price Calculator """

# collect age input from user
# check if the age is under 5, print free
# if age is between 5 - 12, display $5
# if age is between 13 to 64, display $12
# if age is 65 or older, display $8

print('Get your price')

user_age = int(input('Enter Age: '))
print()

if user_age > 0: 
	if user_age < 5: print('Ticket is free')
	if 5 <= user_age <= 12: print('Ticket price is $5')
	if 13 <= user_age <= 64: print('Ticket price is $12')
	if user_age > 65: print('Ticket price is $8')

else: print('Invalid Age')