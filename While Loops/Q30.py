captcha="8452"
entered=input(f"Enter this CAPTCHA code {captcha}: ")
while entered!=captcha:
    print("Incorrect CAPTCHA, try again")
    entered=input(f"Enter this CAPTCHA code {captcha}: ")
print("CAPTCHA solved successfully")
