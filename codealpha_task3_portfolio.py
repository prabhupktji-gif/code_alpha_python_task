# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

total = 0

print("Available stocks:", ", ".join(stocks.keys()))

while True:
    name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if name == "DONE":
        break

    if name not in stocks:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    value = stocks[name] * quantity
    total = total + value

    print(name, "value =", value)

print("\nTotal Investment =", total)

# Save the result
save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    file = open("stock_portfolio.txt", "w")
    file.write("Stock Portfolio\n")
    file.write("----------------\n")
    file.write("Total Investment = " + str(total))
    file.close()

    print("Result saved in stock_portfolio.txt")

print("Thank you!")