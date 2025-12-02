shop_item = input("Please Add your items here(One word only): ")
split_item = shop_item.split()
split_item.sort(key = str.lower)
print(split_item)