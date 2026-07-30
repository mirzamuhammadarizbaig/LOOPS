total=0
count=0
average=0
while average<=35:
    temp=float(input("Enter temperature: "))
    total+=temp
    count+=1
    average=total/count
    print(f"Current average: {average}")
print("Average temperature exceeded 35°C")
