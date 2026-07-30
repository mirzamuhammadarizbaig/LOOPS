import random
captcha=str(random.randint(1000,9999))
print(f"Enter this CAPTCHA code: {captcha}")
entered=input("Your input: ")
while entered!=captcha:
    print("Incorrect CAPTCHA, try again")
    captcha=str(random.randint(1000,9999))
    print(f"Enter this CAPTCHA code: {captcha}")
    entered=input("Your input: ")
print("CAPTCHA solved successfully")
