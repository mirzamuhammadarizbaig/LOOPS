strong = 0
medium = 0
weak = 0

for i in range(1, 21):
    password = input(f"Enter password {i}: ")

    length = len(password)
    has_digit = False
    has_upper = False
    has_special = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True
        if ch in "!@#$%^&*":
            has_special = True

    if length >= 8 and has_digit and has_upper and has_special:
        strong += 1
        print(f"Password {i}: STRONG")
    elif length >= 6 and (has_digit or has_upper):
        medium += 1
        print(f"Password {i}: MEDIUM")
    else:
        weak += 1
        print(f"Password {i}: WEAK")

print("Strong Passwords:", strong)
print("Medium Passwords:", medium)
print("Weak Passwords:", weak)
