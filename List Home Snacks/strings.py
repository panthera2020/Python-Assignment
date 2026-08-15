
def number_of_elements_in(lists):
	
	counter = 0

	for _ in lists:
		counter += 1

	return counter

def return_strings(lists):

	string_array = []

	for index in range(number_of_elements_in(lists)):
		word = lists[index]
		if(number_of_elements_in(word) > 2 and word[0] == word[-1]):
				string_array.append(lists[index])

	return string_array

strings = ["Toy", "Bag", "shoes", "snacks"]

result = return_strings(strings)

print(result)