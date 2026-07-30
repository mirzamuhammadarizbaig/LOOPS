runs=0
wickets=0
counter=0

while True:
    choice=input("Press b to bowl next ball or e to end innings : ")

    if choice=="b":
        if wickets>=10:
            print("All out! Final score is",runs,"for",wickets)
            break

        index=counter%6
        counter=counter+1

        if index==0:
            runs=runs+0
            print("You scored 0 runs")
        elif index==1:
            runs=runs+1
            print("You scored 1 run")
        elif index==2:
            runs=runs+2
            print("You scored 2 runs")
        elif index==3:
            runs=runs+4
            print("You scored 4 runs")
        elif index==4:
            runs=runs+6
            print("You scored 6 runs")
        else:
            wickets=wickets+1
            print("Wicket! Total wickets :",wickets)

        print("Score :",runs,"for",wickets)

    elif choice=="e":
        print("Final score is",runs,"for",wickets)
        break

    else:
        print("Invalid choice")
