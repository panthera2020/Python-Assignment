numbers = [1,2,3,4,5,6,7,8,9,0]

sum_total = 0

for number in range(0,len(numbers),2):
	sum_total += numbers[number]

print(sum_total)
