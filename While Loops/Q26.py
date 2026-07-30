otp="9876"
entered=input("Enter OTP: ")
while entered!=otp:
    print("Incorrect OTP, try again")
    entered=input("Enter OTP: ")
print("OTP Verified")
