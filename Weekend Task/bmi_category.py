""" BMI Category """

# Ask user for weight in kg and height in meters
# Calculate bmi
# If bmi is over 18.5, display underweight
# if bmi is between 18.5 to 24.9, display normal
# if bmi is between 25 to 29.9, display overweight
# if bmi is over 30, display obese

print('Get your BMI category')

user_weight = float(input('Enter weight(kg): '))

user_height = float(input('Enter height(m): '))

bmi = user_weight / (user_height * user_height)

if bmi < 18.5: print('Underweight')

if 18.5 < bmi <= 24.9: print('Normal')

if 25 < bmi <= 29.9: print('Overweight')

if bmi > 30: print('Obese')
