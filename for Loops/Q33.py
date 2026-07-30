total=0
highest=float('-inf')
lowest=float('inf')
for i in range(1,21):
    marks=float(input(f"Enter student {i} marks: "))
    total +=marks
    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks

print("Class Total: ", total)
print("Class average: ",total/20)
print("Class higest: ", highest)
print("Class Lowest: ",lowest)
