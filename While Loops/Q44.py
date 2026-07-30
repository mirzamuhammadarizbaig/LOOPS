rows=5
num=1
i=1
while i<=rows:
    line=""
    j=1
    while j<=i:
        line+=str(num)+" "
        num+=1
        j+=1
    print(line)
    i+=1
