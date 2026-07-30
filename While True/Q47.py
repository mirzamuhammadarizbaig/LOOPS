while True:
    price=input("Enter the price (or type exit) : ")

    if price=="exit":
        print("Thank you for using this program")
        break

    price=int(price)

    if price>5000:
        discount=price*0.2
    elif price>1000:
        discount=price*0.1
    else:
        discount=0

    final_price=price-discount
    print("Discount is",discount)
    print("Final price is",final_price)
