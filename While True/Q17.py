while True:
    celsius=input("Enter temperature in Celsius (or type exit) : ")

    if celsius=="exit":
        print("Thank you for using this program")
        break

    celsius=float(celsius)
    fahrenheit=(celsius*9/5)+32
    print("Temperature in Fahrenheit is",fahrenheit)
