while True:
    basic=input("Enter basic salary (or type exit) : ")

    if basic=="exit":
        print("Thank you for using this program")
        break

    basic=int(basic)
    allowance=basic*0.2
    tax=basic*0.1
    net_salary=basic+allowance-tax

    print("Net salary is",net_salary)
