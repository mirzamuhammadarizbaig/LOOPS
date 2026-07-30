num=0

while True:
    ent=int(input("Enter the number (0 to stop): "))

    num+=ent
    print(num)

    if ent==0:
        break