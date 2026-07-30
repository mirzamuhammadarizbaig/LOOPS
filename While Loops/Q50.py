size=5
matrix=[[0]*size for _ in range(size)]
top=0
bottom=size-1
left=0
right=size-1
num=1
while top<=bottom and left<=right:
    j=left
    while j<=right:
        matrix[top][j]=num
        num+=1
        j+=1
    top+=1
    i=top
    while i<=bottom:
        matrix[i][right]=num
        num+=1
        i+=1
    right-=1
    j=right
    while j>=left and top<=bottom:
        matrix[bottom][j]=num
        num+=1
        j-=1
    bottom-=1
    i=bottom
    while i>=top and left<=right:
        matrix[i][left]=num
        num+=1
        i-=1
    left+=1
i=0
while i<size:
    j=0
    line=""
    while j<size:
        line+=str(matrix[i][j]).rjust(4)
        j+=1
    print(line)
    i+=1
