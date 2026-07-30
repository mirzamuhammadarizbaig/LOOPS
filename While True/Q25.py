while True:
    limit=input("Enter how many even numbers you want (or type exit) : ")

    if limit=="exit":
        print("Thank you for using this program")
        break

    limit=int(limit)
    num=2
    count=0

    while count<limit:
        print(num)
        num=num+2
        count=count+1
