shop_item = input("Please Add your items here(Seperate with comma): ")
split_item = shop_item.split(",")
split_item.sort(key = str.lower)
print(", ".join(split_item))