
answer = int(input('Enter correct number: '))
correct = 0;
incorrect = 0;

while answer != -1: 
	if answer == 1 or answer ==2: correct += 1
	else: incorrect +=1
	answer = int(input('Enter correct number(-1 to quit): '))

print()
print(f'Number of correct: {correct: >3}')
print(f'Number of incorrect: {incorrect: >3}')