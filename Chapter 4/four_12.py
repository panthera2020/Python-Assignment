## Step 1: Set up the starting move
## Step 2: Print the opening message
## Step 3: Random number idea comes in
## Step 4: Update each animal's roll
## Step 5: Draw 70 Squares and add H for each move of hare and T for each move for tortoise
## Step 6: Put all in a loop so the number generation is continues
## Step 7: Stop the loop when theres a winner or when there's a tie, that is when tortoise or hare gets to 70 or above

import random 

tortoise_move = 0

hare_move = 0

print("BANG !!!!! \nAND THEY'RE OFF !!!!!")

print()

while True:
	tortoise_roll = random.randrange(1,11)

	hare_roll = random.randrange(1,11)


	if 1 <= tortoise_roll <=5: tortoise_move += 3

	elif tortoise_roll == 6 or tortoise_roll == 7: tortoise_move += -6

	elif 8 <= tortoise_roll <= 10: tortoise_move += 1

	if tortoise_move < 1: tortoise_move = 1


	if hare_roll == 1 or hare_roll == 2: hare_move += 0

	elif hare_roll == 4 or hare_roll == 3: hare_move += +9

	elif hare_roll == 5: hare_move -= 12

	elif 6 <= hare_roll <= 8 : hare_move += 1

	elif hare_roll == 9 or hare_roll == 10: hare_move -= 2

	if hare_move < 1: hare_move = 1


	line = ''
	for square in range(1, 71):
		if square == tortoise_move and square == hare_move: line += 'OUCH!!!'

		elif square == tortoise_move: line += 'T'

		elif square == hare_move: line += 'H'

		else: line += '-'

		# line += ''

	print(line)

	if hare_move >= 70 and tortoise_move < 70:
		print()
		print('Hare is the winner!!!')
		break
	elif tortoise_move >= 70 and hare_move < 70:
		print()
		print('Tortoise is the winner')
		break
	elif tortoise_move >= 70 and hare_move >=70:
		print()
		print('Its a tie!!!')
		break
