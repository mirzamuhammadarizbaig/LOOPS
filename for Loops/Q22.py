count=0
for i in range(10):
    num=float(input(f"Enter your number {i+1}: "))
    if num==0:
        count+=1

print("Zeros are: ",count)