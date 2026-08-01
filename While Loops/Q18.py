count=0
num=int(input("Enter a number (0 to stop): "))
while num!=0:
    if num>1:
        isprime=True
        i=2
        while i<num:
            if num%i==0:
                isprime=False
            i+=1
        if isprime:
            count+=1
    num=int(input("Enter a number (0 to stop): "))
print(f"Prime numbers entered: {count}")
