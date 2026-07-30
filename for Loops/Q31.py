presentCount=0
for i in range(1,31):
    present=input(f"Is student {i} present? (yes/no): ").lower()
    if present=="yes":
        presentCount+=1
print(f"{presentCount} Students are present today")