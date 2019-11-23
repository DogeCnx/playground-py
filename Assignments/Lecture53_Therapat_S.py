def vatCal(price):
    result = price+(price*7/100)
    return result
price = int(input("Total Price::"))
print(vatCal(price))
