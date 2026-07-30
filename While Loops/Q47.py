num=2
while num<=1000:
    isprime=True
    i=2
    while i<num:
        if num%i==0:
            isprime=False
            break
        i+=1
    if isprime:
        print(num)
    num+=1
