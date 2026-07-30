while True:
    num=input("Enter a number (or type exit) : ")

    if num=="exit":
        print("Thank you for using this program")
        break

    num=int(num)
    fact=1
    i=1

    while i<=num:
        fact=fact*i
        i=i+1

    print("Factorial is",fact)
