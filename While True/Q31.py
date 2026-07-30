score=0

while True:
    question=input(
        "What is the capital of France?\n"
        "(type exit to quit)\n"
    )

    if question=="exit":
        print("Your final score is",score)
        break

    if question=="paris":
        print("Correct answer")
        score=score+1
    else:
        print("Wrong answer")
