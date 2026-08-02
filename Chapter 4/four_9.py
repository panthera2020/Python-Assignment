""" Temprature Conversion """

def faren(celcius):
	return ((9 / 5) * celcius) + 32

print(f'{'Celcius': ^15} {'Farenheit': ^15}')
for numbers in range(1, 101):
	print(f'{numbers: >9}°C {faren(numbers): >14.2f}°F')