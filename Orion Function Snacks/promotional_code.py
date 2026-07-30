""" Check for promotional code and give discount """

def promo(product, price, promo_code):
	promo_code = promo_code.upper()

	if promo_code == 'SAVE10': discount_price = price - (price * 0.1)
	elif promo_code == 'HALFOFF': discount_price = price - (price * 0.5)
	elif promo_code != 'SAVE10' and promo_code != 'HALFOFF': discount_price = price 

	return discount_price


