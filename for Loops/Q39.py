n=int(input("How many transactions?: "))
balance=2000

for i in range(1,n+1):
    type=input("Deposit or withdraw?: ").lower()
    amount=float(input(f"Enter the amount you want to {type}: "))
    if type=="deposit":
        balance+=amount
    else:
        if amount>balance:
            print("Insufficiant funds")
        else:
            balance-=amount
        print("Current Balance =",balance)
print("Final Balance =",balance)