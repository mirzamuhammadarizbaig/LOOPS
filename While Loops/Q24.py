password=input("Enter a password: ")
valid=False
while not valid:
    hasupper=False
    haslower=False
    hasdigit=False
    i=0
    while i<len(password):
        ch=password[i]
        if ch.isupper():
            hasupper=True
        elif ch.islower():
            haslower=True
        elif ch.isdigit():
            hasdigit=True
        i+=1
    if hasupper and haslower and hasdigit:
        valid=True
    else:
        print("Password must contain uppercase, lowercase and a digit")
        password=input("Enter a password: ")
print("Password accepted")
