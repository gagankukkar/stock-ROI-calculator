from decimal import Decimal

nextStep = "redo"

while nextStep == "redo" or nextStep == "more":
    if nextStep == "redo":
        ticker = input("Enter ticker name: ").upper()
        commission = round(Decimal(input("Enter buying/selling commission: ")), 2)
        price = [[]]
        numPurchase = 0
        sharePriceTot = Decimal(0.00)
        sharesTot = 0

    if nextStep == "more":
        price.append([])

    price[numPurchase].append(int(input("Enter number of shares purchased: ")))
    price[numPurchase].append(round(Decimal(input("Enter stock price: ")), 2))

    sharesTot += price[numPurchase][0]
    sharePriceTot += price[numPurchase][0] * price[numPurchase][1]

    buyTot = sharePriceTot + (commission * (len(price)+1))

    sellBE = buyTot / sharesTot
    sell5 = sellBE * Decimal(1.05)
    sell10 = sellBE * Decimal(1.10)
    sell15 = sellBE * Decimal(1.15)
    sell20 = sellBE * Decimal(1.20)

    numPurchase += 1

    def stats():
        print("-----------------------------------------------")
        print("ROI for stock: " + ticker)
        print(f"Number of buying transactions: {numPurchase}")
        print(f"Commission charged per transaction: ${commission}\n")
        print(f"Break-even selling price: ${round(sellBE, 2)}")
        print(f"Selling price for 5% ROI: ${round(sell5, 2)}")
        print(f"Selling price for 10% ROI: ${round(sell10, 2)}")
        print(f"Selling price for 15% ROI: ${round(sell15, 2)}")
        print(f"Selling price for 20% ROI: ${round(sell20, 2)}")

    stats()

    print("\nType 'more' to add more share purchases or 'redo' to start over for a new stock.")
    nextStep = input("Type any other key to exit: ")

print("Have a great day!")
