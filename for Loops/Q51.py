deposits = 0
withdrawals = 0
balance = 0
highest = 0

for i in range(1, 21):
    ttype = input(f"Transaction {i} - Enter type (deposit/withdraw): ")
    amount = float(input(f"Enter amount: "))

    if ttype.lower() == "deposit":
        deposits += amount
        balance += amount
    else:
        withdrawals += amount
        balance -= amount

    if amount > highest:
        highest = amount

    print(f"Transaction {i}: {ttype} of {amount}")

print("Total Deposits:", deposits)
print("Total Withdrawals:", withdrawals)
print("Final Balance:", balance)
print("Highest Transaction:", highest)
