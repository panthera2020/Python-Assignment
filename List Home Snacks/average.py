
numbers = [1,2,3,4,5,6,7,8,9,0]

total = 0

for number in range(len(numbers)):
	total += numbers[number]

average = total / len(numbers)

print("The average is ", average)