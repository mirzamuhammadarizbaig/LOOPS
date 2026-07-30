heads=0
flips=0
while heads<5:
    flip=input("Enter the flip result (heads/tails): ")
    flips+=1
    if flip=="heads":
        heads+=1
    else:
        heads=0
print(f"Got 5 heads in a row after {flips} flips")
