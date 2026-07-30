while True:
    num=input("Enter a number (or type exit) : ")

    if num=="exit":
        print("Thank you for using this program")
        break

    num=int(num)
    is_prime=True
    i=2

    if num<2:
        is_prime=False

    while i<num:
        if num%i==0:
            is_prime=False
        i=i+1

    if is_prime==True:
        print("Prime number")
    else:
        print("Not a prime number")
