import random
speed=5
distance=0
alive=True
while alive:
    distance+=speed
    speed+=1
    print(f"Distance: {distance}, Speed: {speed}")
    if random.randint(1,10)==1:
        alive=False
print(f"You crashed! Final distance: {distance}")
