username=input("Enter a username: ")
while len(username)<8:
    print("Username must be at least 8 characters")
    username=input("Enter a username: ")
print(f"Username accepted: {username}")
