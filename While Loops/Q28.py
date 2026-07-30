oldpassword="oldpass1"
newpassword=input("Enter a new password: ")
while newpassword==oldpassword:
    print("New password cannot be the same as the previous password")
    newpassword=input("Enter a new password: ")
print("Password changed successfully")
