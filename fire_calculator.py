balance = int(input("Please enter your balance: "))
target_balance = int(input("Please eneter your target amount: "))
years = 0

while balance < target_balance:
    balance *= 1.05
    years += 1
    print(f"Status: Balance {int(balance)}, {years} years")

print(f"It took you {years} years, to double your money")


 