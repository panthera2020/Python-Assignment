""" Approximating the mathematical Constant e """

e = 1 
factorial = 1

for numbers in range(1, 100):
	factorial = 1
	for number in range(numbers, 0, -1):
		factorial *= number
	e += 1 / factorial

print(f'{e:.2f}, {e:.3f}, {e:.4f}, {e:.5f}')