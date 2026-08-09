

def box_number_for(number_of_guest, pizza_type):

	number_of_box = 0

	if pizza_type.lower() == 'odogwu': number_of_box = (number_of_guest // 12) + 1

	elif pizza_type.lower() == 'big boys': number_of_box = (number_of_guest // 8) + 1

	elif pizza_type.lower() == 'small money': number_of_box = (number_of_guest // 6) + 1

	elif pizza_type.lower() == 'sapa size': number_of_box = (number_of_guest // 4) + 1

	return number_of_box


def slices_left_in(number_of_guest, pizza_type):

	number_of_slice = 0

	if pizza_type.lower() == 'odogwu': number_of_slice = (box_number_for(number_of_guest, pizza_type) * 12) - number_of_guest

	elif pizza_type.lower() == 'big boys': number_of_slice = (box_number_for(number_of_guest, pizza_type) * 8) - number_of_guest

	elif pizza_type.lower() == 'small money': number_of_slice = (box_number_for(number_of_guest, pizza_type) * 6) - number_of_guest

	elif pizza_type.lower() == 'sapa size': number_of_slice = (box_number_for(number_of_guest, pizza_type) * 4) - number_of_guest

	return number_of_slice

def price_for(number_of_guest, pizza_type):

	price_of_box = 0

	if pizza_type.lower() == 'odogwu': price_of_box = box_number_for(number_of_guest, pizza_type) * 5200

	elif pizza_type.lower() == 'big boys': price_of_box = box_number_for(number_of_guest, pizza_type) * 4000

	elif pizza_type.lower() == 'small money': price_of_box = box_number_for(number_of_guest, pizza_type) * 2900

	elif pizza_type.lower() == 'sapa size': price_of_box = box_number_for(number_of_guest, pizza_type) * 2500

	return price_of_box 

def is_valid_pizza(pizza_type):

	is_valid = False 

	if pizza_type.lower() == 'odogwu': is_valid = True

	elif pizza_type.lower() == 'big boys': is_valid = True

	elif pizza_type.lower() == 'small money': is_valid = True

	elif pizza_type.lower() == 'sapa size': is_valid = True

	return is_valid