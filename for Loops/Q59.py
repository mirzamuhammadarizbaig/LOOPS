total_payroll = 0
overtime_rate = 200

for i in range(1, 31):
    name = input(f"Enter name of employee {i}: ")
    basic = float(input(f"Enter basic salary for {name}: "))
    overtime_hours = float(input(f"Enter overtime hours for {name}: "))
    bonus = float(input(f"Enter bonus for {name}: "))

    overtime_pay = overtime_hours * overtime_rate
    salary = basic + overtime_pay + bonus
    total_payroll += salary

    print(f"{name}: Salary={salary}")

print("Total Payroll:", total_payroll)
