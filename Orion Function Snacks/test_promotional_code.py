from promotional_code import promo 

print('Give the price of your item, get dicount if you have a valid promo code')

print()

user_product_input = input('Enter item: ')

user_price_input = int(input('Enter price of item: '))

user_promo_code_input = input('Enter promo code: ')

new_price = promo(user_product_input, user_price_input, user_promo_code_input)

print()

print(new_price)