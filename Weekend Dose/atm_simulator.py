""" An ATM simulator """

balance = 1000

while True:
	print()
	print()
	user_input = int(input("""

Deposit -> Enter 1
Withdraw -> Enter 2
Balance -> Enter 3

Exit -> Enter 0

"""))

	print()

	match user_input:
		case 1 : 
			user_amount = int(input('Enter amount: '))

			print()

			if user_amount > 0: balance += user_amount

			elif user_amount < 0: print('Enter valid amount')
		case 3 :
			print('Your Balance: ', balance)
		case 2 : 
			user_withdrawal_amount = int(input('Enter amount: '))

			print()

			if user_withdrawal_amount > balance : print('Insufficient Balance')
			
			elif user_withdrawal_amount <= balance :
				balance -= user_withdrawal_amount
				print('Transaction Complete!!!')
				print()
				print('Your Balance: ',balance)
		case 0 : break
		case _ : print('Invalid Input') 
		