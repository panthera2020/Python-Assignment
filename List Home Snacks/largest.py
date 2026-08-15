
numbers = [2,13,4,6,1,33,29,9]

largest = numbers[0]

for number in range(1,len(numbers)):
	if numbers[number] > largest : largest = numbers[number]

print("Largest is: ",largest).