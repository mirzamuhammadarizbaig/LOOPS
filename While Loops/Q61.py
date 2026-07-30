counts={}
num=input("Enter a number: ")
counts[num]=1
while counts[num]<3:
    num=input("Enter a number: ")
    if num in counts:
        counts[num]+=1
    else:
        counts[num]=1
print(f"The number {num} appeared three times")
