size=5
i=1
while i<=size:
    j=1
    line=""
    while j<=size:
        if i==1 or i==size or j==1 or j==size:
            line+="*"
        else:
            line+=" "
        j+=1
    print(line)
    i+=1
