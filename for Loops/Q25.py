a=int(input("Enter your first value: "))
b=int(input("Enter your second value: "))

start, end = min(a,b), max(a,b)
for i in range(start, end +1):
    print(i, end="")

print()