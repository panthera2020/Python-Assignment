
def sum_third_elements_in(lists):
	total = 0

	for index in range(2,len(lists),3):

		total += lists[index]

	return total


numbers = [12,3,20,4,6,11,15,33,17,22,1,12]

result = sum_third_elements_in(numbers)

print(result)