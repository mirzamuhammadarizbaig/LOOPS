size=8
i=0
while i<size:
    j=0
    line=""
    while j<size:
        if (i+j)%2==0:
            line+="*"
        else:
            line+=" "
        j+=1
    print(line)
    i+=1
