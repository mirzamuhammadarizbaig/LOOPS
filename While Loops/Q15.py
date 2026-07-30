entered=[]
num=int(input("Enter a number: "))
while num not in entered:
    entered.append(num)
    num=int(input("Enter a number: "))
print(f"Duplicate number entered: {num}")
