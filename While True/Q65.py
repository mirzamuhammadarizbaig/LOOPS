correct_code="0000"
alarm_armed=True

while True:
    if alarm_armed==True:
        code=input("Enter security code to disarm (or type exit) : ")

        if code=="exit":
            print("Thank you for using this program")
            break

        elif code==correct_code:
            alarm_armed=False
            print("Alarm disarmed")

        else:
            print("ALERT! Wrong code entered")

    else:
        choice=input("Alarm is disarmed. Type arm to arm it again or exit to quit : ")

        if choice=="arm":
            alarm_armed=True
            print("Alarm armed")

        elif choice=="exit":
            print("Thank you for using this program")
            break

        else:
            print("Invalid choice")
