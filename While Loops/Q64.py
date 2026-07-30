found=False
symbols="!@#$%^&*"
while not found:
    password=input("Enter a password: ")
    hasupper=False
    haslower=False
    hasdigit=False
    hassymbol=False
    i=0
    while i<len(password):
        ch=password[i]
        if ch.isupper():
            hasupper=True
        elif ch.islower():
            haslower=True
        elif ch.isdigit():
            hasdigit=True
        elif ch in symbols:
            hassymbol=True
        i+=1
    if hasupper and haslower and hasdigit and hassymbol:
        found=True
    else:
        print("Password must contain uppercase, lowercase, digit and symbol, try again")
print(f"Valid password accepted: {password}")
