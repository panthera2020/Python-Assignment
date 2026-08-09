from pizza_wahala import *

print('Welcome to Iya Honour Pizza Joint')

print("""

*************************************************
* 	Pizza Type	 *	 Price per Box	*
*************************************************
*	Sapa size	 *		2500	*
*	Small Money	 *		2900	*
*	Big Boys	 *		4000	*
*	Odogwu		 *		5200	*
*************************************************
	""")

print()

guest_number = int(input('Enter Number of Guest: '))

print()

pizza_type = input('Enter Pizza Type: ')

print()

if is_valid_pizza(pizza_type) :
	print(f'Number of Boxes to buy: {box_number_for(guest_number, pizza_type)}')

	print(f'Number of Left over slices after serving: {slices_left_in(guest_number, pizza_type)}')

	print(f'Price: {price_for(guest_number, pizza_type)}')
else:
	print('Invalid input. \n Try again.')