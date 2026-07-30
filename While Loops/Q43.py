rows=5
i=0
while i<rows:
    num=1
    j=0
    line=""
    while j<=i:
        line+=str(num)+" "
        num=num*(i-j)//(j+1)
        j+=1
    print(line)
    i+=1
