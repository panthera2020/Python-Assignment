""" Determine is user is a child, teen or adult """

# Collect users age 
# if user age is less than 13, display child
# if user age is between 13 to 20, Display Teen 
# if user age is greater than 20, Display Adult

print('Get your Age Category')

user_age = int(input('Enter your age: '))

print()

if user_age < 13: print('Child')

elif 13 <=user_age < 20: print('Teen')

elif user_age >= 20: print('Adult')