light="red"
running=True
while running:
    print(f"Light is {light}")
    if light=="red":
        light="green"
    elif light=="green":
        light="yellow"
    elif light=="yellow":
        light="red"
    choice=input("Press q to quit or Enter to continue: ")
    if choice=="q":
        running=False
print("Traffic light simulation stopped")
