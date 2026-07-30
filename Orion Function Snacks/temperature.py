""" A function that converts celcius to farenhiet and vice versa amd give heat advisory """

def temp(number, c_or_f ):
	celcius_or_farenheit = c_or_f.lower()

	temprature_treshold_in_celcius = 32

	if celcius_or_farenheit == 'f': 
		temprature_in_celcius = (number - 32)  * (5 / 9)

		if temprature_in_celcius >= temprature_treshold_in_celcius: return 'Heat alert'

		elif temprature_in_celcius < temprature_treshold_in_celcius: return 'Cold Advisory'

	elif celcius_or_farenheit == 'c':
		if number >= temprature_treshold_in_celcius: return 'Heat Alert'
		
		elif number < temprature_treshold_in_celcius: return 'Cold Advisory' 



