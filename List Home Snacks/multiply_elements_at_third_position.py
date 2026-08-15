numbers = [1,2,3,4,5,6,7,8,9,0]

product = 1

for number in range(0,len(numbers),2):
	product *= numbers[number]

print(product)
