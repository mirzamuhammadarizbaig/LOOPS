namaz=0
for i in range(5):
    pray=input(f"Have your prayed namaz {i+1}: ").lower()
    if pray=="yes":
        namaz+=1
print(f"You prayed {i}/5 namaz")