usedletters=[]
name=input("Enter a name: ")
firstletter=name[0].lower()
usedletters.append(firstletter)
while True:
    name=input("Enter a name: ")
    firstletter=name[0].lower()
    if firstletter in usedletters:
        print("This letter has already been used, stopping")
        break
    usedletters.append(firstletter)
