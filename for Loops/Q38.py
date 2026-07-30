n=int(input("Enter the number of students: "))
Pass=0
fail=0

for i in range(1,n+1):
    name=input(f"Enter student {i} name: ")
    marks=int(input(f"Enter {name} marks: "))
    if marks>40:
        status="pass"
        Pass+=1
    else:
        status="fail"
        fail+=1
    print(name, marks, status)
print(f"Total Students pass = {Pass}")
print(f"Total Students fail = {fail}")