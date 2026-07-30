n=int(input("How many employees?: "))
totalSalary=0

for i in range(1,n+1):
    name=input(f"Enter employee {i} name: ")
    basicPay=float(input(f"Enter the basic pay amount for employee {i}: "))
    bonus=int(input("Enter the bonus amount: "))
    netSalary= basicPay+bonus
    print(f"{name} salary is {netSalary}")
    totalSalary+=netSalary
print("Total Salary", totalSalary)
