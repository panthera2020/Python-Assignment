
def sum_of_first_middle_last_element(lists):
	total = 0
	length = len(lists) 
	if(length % 2 != 0):
		middle_index = length // 2 

		total = lists[0] + lists[middle_index] + lists[-1]

	elif (length % 2  == 0): 
		average_of_middle_elements = (lists[length // 2] + lists[(length // 2) - 1]) / 2

		total = lists[0] + average_of_middle_elements + lists[-1]

	return total


even_list = [2,3,5,6]

odd_list = [1,2,3,4,5]

first_result = sum_of_first_middle_last_element(even_list)

second_result = sum_of_first_middle_last_element(odd_list)

print(first_result)

print()

print(second_result)