import random
heads=0
flips=0
while heads<5:
    flip=random.choice(["heads","tails"])
    flips+=1
    print(f"Flip {flips}: {flip}")
    if flip=="heads":
        heads+=1
    else:
        heads=0
print(f"Got 5 heads in a row after {flips} flips")
