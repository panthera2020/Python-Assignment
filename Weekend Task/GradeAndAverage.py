""" Calculate average and return values of associated grades """

# Question 2
# collect three scores 
# use and if statment to only collect inputs between 0 and 100
# use loop to collect tha input three times
# use if statement to check if grade falls between A, B, C, D, F
# initialize sum, then add each of the scores to get the total sum
# divide the sum by three to get the average
# Display average

import sys

print("Get the grade of Three Scores")

first_score = int(input('Enter First Score: '))

if 0 < first_score <= 100:
	if 90 <= first_score <= 100: print('Grade is A')
	elif 80 <= first_score < 90: print('Grade is B')
	elif 70 <= first_score < 80: print('Grade is B')
	elif 60 <= first_score < 70: print('Grade is B')
	elif 0 <= first_score < 60: print('Grade is B')

else: 
	print('Invalid Input') 
	sys.exit(0)

second_score = int(input('Enter Second Score: '))

if 0 < second_score <= 100:
	if 90 <= second_score <= 100: print('Grade is A')
	elif 80 <= second_score < 90: print('Grade is B')
	elif 70 <= second_score < 80: print('Grade is B')
	elif 60 <= second_score < 70: print('Grade is B')
	elif 0 <= second_score < 60: print('Grade is B')

else: 
	print('Invalid Input') 
	sys.exit(0)

third_score = int(input('Enter Third Score:'))

if 0 < third_score <= 100:
	if 90 <= third_score <= 100: print('Grade is A')
	elif 80 <= third_score < 90: print('Grade is B')
	elif 70 <= third_score < 80: print('Grade is B')
	elif 60 <= third_score < 70: print('Grade is B')
	elif 0 <= third_score < 60: print('Grade is B')

else: 
	print('Invalid Input') 
	sys.exit(0)

average = (first_score + second_score + third_score) / 3

print()
print('Average:', average)