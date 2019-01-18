import time
import random

print('A wild Metapod appears')
time.sleep(0.3)
print('... the background music changes...')
time.sleep(0.3)
print('You only have one Pokemon, Charmander!')
time.sleep(0.3)
print('I choose you Charmander!!!')
time.sleep(0.3)
print()

# set the starting health values
Charmander_hp = 200
Metapod_hp = 600

player_move = input('Pick a move using the corresponding number: ')
player_move = int(player_move)
if player_move == 1:
	Charmander_hp = Charmander_hp - 25
	print('Metapod uses Tackle 👊 and deals 25 HP of damage.')
elif player_move == 2:
	damage = random.radint(5,40)
	Charmander_hp = Charmander_hp - damage
	print('Charmander uses Fire Blast 💥 and deals ' +str(damage) + 'HP of damage.')
elif player_move == 3:
	Charmander_hp = Charmander_hp + 100
	print('Charmander uses Growl 🗣 and recovers 100 HP.')

time.sleep(0.3)
print()





while Charmander_hp > 0 and Metapod_hp > 0:
	print('Choose your battle move: ')
	time.sleep(0.3)
	print('- [1] Tackle 👊')
	time.sleep(0.3)
	print('- [2] Fire Blast 💥')
	time.sleep(0.3)
	print('- [3] Growl 🗣')
	time.sleep(0.3)
	print('- [4] Scratch 💅')
	time.sleep(0.3)
	print()


time.sleep(0.3)
print()

#enemy battle choices
enemy_move = random.radint(1,2)
if enemy_move == 1:
	Charmander_hp = Charmander_hp - 30
	print('Metapod uses Drink Blood and deals 30 HP of damage')
elif enemy_move == 2:
	Charmander_hp = Charmander_hp - 20
	Metapod_hp = Metapod_hp + 20
	print('Metapod uses Drink Blood and deals 20 HP of damage while also recovering 20 HP of health')

time.sleep(0.3)
print()
#check and avoid negative HP
if Charmander_hp   < 0:
	Charmander_hp = 0

if Metapod_hp < 0:
	Metapod_hp = 0

#display the current healths
print('Update HP:')
print('Charmander HP:' +str(Charmander_hp))
print('Metapod HP:' +str(Metapod_hp))
time.sleep(0.3)
print()
#check who won
if Metapod_hp > 0 and Charmander_hp= 0:
	print('Charmander has won!')
if Charmander_hp > 0 and Metapod_hp= 0:
	print('Metapod has won!')
print('Pokémon by Xavier Souffront')