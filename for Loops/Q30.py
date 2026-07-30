smallest = float('inf')
for i in range(10):
    num = float(input(f"Number {i+1}: "))
    if num < smallest:
        smallest = num
print("Smallest:", smallest)