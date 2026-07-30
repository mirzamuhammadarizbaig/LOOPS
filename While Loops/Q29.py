code=input("Enter a 6 digit security code: ")
while len(code)!=6 or not code.isdigit():
    print("Security code must be exactly 6 digits")
    code=input("Enter a 6 digit security code: ")
print(f"Security code accepted: {code}")
