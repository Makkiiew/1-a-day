import random

makkiiew_option = input("Makkiiew: Input 3 Resturants to choose(seperate with comma): ")
acchan_option = input("Acchan: Input 3 Resturants to choose(seperate with comma): ")
split_makkiiew_option = makkiiew_option.split(",")
split_acchan_option = acchan_option.split(",")
all_option = split_makkiiew_option + split_acchan_option
all_option.sort()
print(all_option)
option = random.choice(all_option)
print(f"Fate has spoken. Tonight we eat: {option}.")