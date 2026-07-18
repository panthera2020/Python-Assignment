""" Rock-Paper-Scissor (One Round) """

# Ask each player to choose between rock, paper, scissors
# if user1 choose rock and  user2 chooses scissor user 1 wins, but other other user chooses paper user2 wins
# then else 
# if user1 chooses paper and user2 chooses rock user1 wins, but if user2 chooses scissors user 2 wins
# then else
# if user1 chooses scissors and user 2 chooses paper user1 wins, but if user2 chooses rock user 1 wins
# then else

print('Rock-Paper-Scissor')

print()

print('Choose either, rock, paper or scissors')

player_one = input('Player 1: ')

player_two = input('Player 2: ')

print()

if player_one == 'rock' and player_two == 'scissors': print('Player 1 wins')
elif player_one == 'rock' and player_two == 'paper': print('Player 2 wins')
elif player_two == 'rock' and player_one == 'scissors': print('Player 2 wins')
elif player_two == 'rock' and player_one == 'paper': print('Player 1 wins')

elif player_one == 'paper' and player_two == 'rock': print('Player 1 wins')
elif player_one == 'paper' and player_two == 'scissors': print('Player 2 wins')
elif player_two == 'paper' and player_one == 'rock': print('Player 2 wins')
elif player_two == 'paper' and player_one == 'scissors': print('Player 1 wins')

elif player_one == 'scissors' and player_two == 'paper': print('Player 1 wins')
elif player_one == 'scissors' and player_two == 'rock': print('Player 2 wins')
elif player_two == 'scissors' and player_one == 'paper': print('Player 2 wins')
elif player_two == 'scissors' and player_one == 'rock': print('Player 1 wins')

elif player_one == 'scissors' and player_two == 'scissors': print('Tie')
elif player_one == 'rock' and player_two == 'rock': print('Tie')
elif player_one == 'paper' and player_two == 'paper': print('Tie')

else: print('Invalid input')