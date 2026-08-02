print(f'{'number': ^10}{'square': ^10}{'cube': ^10}')

for numbers in range(6):
	print(f'{numbers: >8}{numbers **2: >10}{numbers **3: >9}')