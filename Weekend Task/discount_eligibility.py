""" Discount Eligiblity """

# Ask for user total bill 
# ask if user is a member or not
# if total bill is greater or equal to 1000 and is a member 10% off, Display final amount and discout message
# if total bill is greater or equal to 1000 and is a not a member 5% off, Display final amount and discout message
# Else no discount, print final amount

print('Discount Eligibility')

user_total_bill = int(input('Enter total bill: '))

is_member = input('Are you a member?(yes/no): ')

print()

if user_total_bill >= 1000 and is_member == 'yes':
	discount = user_total_bill * 0.1
	final_amount = user_total_bill - discount
	print('Final amount: ', final_amount, '\n10% Discount')

elif user_total_bill >= 1000 and is_member == 'no':
	discount = user_total_bill * 0.05
	final_amount = user_total_bill - discount
	print('Final amount: ', final_amount, '\n5% Discount')

else: print(user_total_bill, '\nNo Discount')