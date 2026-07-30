counter=0

while True:
    guess=input("Guess heads or tails (or type exit) : ")

    if guess=="exit":
        print("Thank you for playing")
        break

    index=counter%2
    counter=counter+1

    if index==0:
        result="heads"
    else:
        result="tails"

    if guess==result:
        print("Correct! It was",result)
    else:
        print("Wrong! It was",result)
