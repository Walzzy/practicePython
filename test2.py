game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
player_a = str(input("Player a: "))
player_b = str(input("Player b: "))
a = game_dict.get(player_a)
b = game_dict.get(player_b)
print(type(a))
print(type(b))
dif = a - b
print(dif)
print(type(dif))

if dif in [-1, 2]:
    print('player a wins.')
else:
    print("you lose")
