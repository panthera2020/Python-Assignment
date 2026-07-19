""" Different greeeting for different users based on lenght of their name """

# Collect user name 
# if name length is between 3 and 5, Display hi name
# if name lenght is greater than 5, Display Hello name

user_name = input('Enter name: ')

print()

if 3 <= len(user_name) <= 5: print('Hi', user_name)
if len(user_name)> 5: print('Hello', user_name)