racer1=0
racer2=0
finish=50
while racer1<finish and racer2<finish:
    move1=int(input("Enter Racer 1's move: "))
    move2=int(input("Enter Racer 2's move: "))
    racer1+=move1
    racer2+=move2
    print(f"Racer 1: {racer1}, Racer 2: {racer2}")
if racer1>=finish and racer2>=finish:
    print("It's a tie!")
elif racer1>=finish:
    print("Racer 1 wins!")
else:
    print("Racer 2 wins!")
