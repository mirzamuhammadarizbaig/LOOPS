import random
import string
found=False
while not found:
    password=""
    i=0
    while i<8:
        password+=random.choice(string.ascii_letters+string.digits+string.punctuation)
        i+=1
    hasupper=False
    haslower=False
    hasdigit=False
    hassymbol=False
    j=0
    while j<len(password):
        ch=password[j]
        if ch.isupper():
            hasupper=True
        elif ch.islower():
            haslower=True
        elif ch.isdigit():
            hasdigit=True
        elif ch in string.punctuation:
            hassymbol=True
        j+=1
    print(f"Generated: {password}")
    if hasupper and haslower and hasdigit and hassymbol:
        found=True
print(f"Valid password found: {password}")
