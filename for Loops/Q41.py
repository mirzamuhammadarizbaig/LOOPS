n = int(input("How many people want to buy ticket for Spider Man BND: "))
tickets = 20
totalSold = 0

for i in range(1, n+1):
    customer = int(input(f"How many tickets customer {i} wants to buy?: "))
    if customer > tickets:
        print("House Full, only", tickets, "tickets left")
    else:
        tickets -= customer
        totalSold += customer
        print(f"Customer {i} bought {customer} tickets")

print("Total", totalSold, "sold")
print("Tickets remaining:", tickets)