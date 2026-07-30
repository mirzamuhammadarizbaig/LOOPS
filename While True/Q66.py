daily_limit=50000
total_withdrawn=0

while True:
    amount=input("Enter withdrawal amount (or type exit) : ")

    if amount=="exit":
        print("Thank you for using this program")
        break

    amount=int(amount)

    if amount>20000:
        print("ALERT! Suspicious transaction detected")
    elif total_withdrawn+amount>daily_limit:
        print("Transaction blocked, daily limit exceeded")
    else:
        total_withdrawn=total_withdrawn+amount
        print("Transaction successful, total withdrawn today is",total_withdrawn)
