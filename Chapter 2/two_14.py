""" Target Heart-Rate Calculator """

# Ask user for age
# Calculate the maximum heart rate using the formula 220 minus age in years
# calulate for minimum target, maximum heart rate multipled by 0.5
# Calculate for maximum target, maximum heart rate multiplied by 0.8
# Display maximum heart rate and range of users target heart rate 

user_age = int(input('Enter your age(years): '))

user_minimum_target = 220 - user_age

user_minimum = user_minimum_target * 0.5

user_maximum = user_minimum_target * 0.8

print('Your Maximum Heart Rate: ', user_minimum_target)

print('Range: ', user_minimum, '-', user_maximum)