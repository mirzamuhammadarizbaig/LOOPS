while True:
    num=input("Enter a number (or type exit) : ")

    if num=="exit":
        print("Thank you for using this program")
        break

    original=int(num)
    temp=original
    reverse=0

    while temp!=0:
        digit=temp%10
        reverse=(reverse*10)+digit
        temp=temp//10

    if original==reverse:
        print("Palindrome number")
    else:
        print("Not a palindrome number")
