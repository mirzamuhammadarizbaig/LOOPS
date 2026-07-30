total=0

while True:
    item=input("Enter item name (or type done to finish) : ")

    if item=="done":
        print("Your total bill is",total)
        break

    price=int(input("Enter price : "))
    qty=int(input("Enter quantity : "))
    total=total+(price*qty)
