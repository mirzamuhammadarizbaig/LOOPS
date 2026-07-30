speed=5
distance=0
alive=True
while alive:
    distance+=speed
    speed+=1
    print(f"Distance: {distance}, Speed: {speed}")
    collision=input("Did you crash? (yes/no): ")
    if collision=="yes":
        alive=False
print(f"You crashed! Final distance: {distance}")
