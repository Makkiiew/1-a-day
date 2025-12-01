inventory = ["Sword", "Potion", "Map", "Spell Book - FireBolt"]
inventory.append("Shield")
drop = inventory.pop()
print(f'You open your bag. The first item is {inventory[0]} and the last item is {inventory[-1]}. You have also just dropped your {drop}')
goblin_attack = inventory.pop()
print(f'Oh no Goblin appears you use your {goblin_attack}')
inventory.insert(2, "10 Gold")
print(f'This is what you have left in your inventory{inventory}')