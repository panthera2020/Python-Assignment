""" Approximating the Mathematical Constant PI """

pi = 4

for numbers in range(3, 10000, 2):
	if(((numbers - 3) // 2 ) % 2 == 0): pi -= (4 / numbers)
	else: pi += (4 / numbers)
	

print(f'{pi:.2f}, {pi:.3f}, {pi:.4f}, {pi:.5f}')