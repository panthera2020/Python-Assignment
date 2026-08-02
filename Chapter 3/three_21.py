""" Calculate change using fewest number of coins """

# Penny: Worth 1 cent 
# Dime: Worth 10 cents 
# Quarter: Worth 25 cents 

print('Get your change')

print()

user_purchase = float(input('Enter price of items bought($1 or less): '))

user_payment = float(input('Enter payment($): '))

balance = 0

if 0 < user_payment <= 1 and 0 < user_purchase <= 1 and user_payment > user_payment: balance = user_payment - user_purchase

else: print('Invalid input')

change = balance * 100

quarters = change // 25

dimes = (change - (quarters * 25)) // 10

pennies = change - ((quarters * 25) + (dimes * 10))

print()

print(f'Your change is: \n{quarters} quarters\n{dimes} dimes\n{pennies} pennies')