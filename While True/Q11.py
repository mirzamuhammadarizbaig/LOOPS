even=0
odd=0

while True:
    num=int(input("Enter your number: "))
    if num==0:
        break
    elif num %2<=0:
        print(f"This number is even {num}")
    else:
        print(f"The number is odd {num}")