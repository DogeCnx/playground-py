def login():
    user = input("Username :")
    password = input("Password :")
    if user == "doge" and password == "wow":
        return True
    else:
        return False


def showMenu():
    print("-----DogeSystem-----")
    print("1. Vat calculator")
    print("2. Price calculator")


def menuSelect():
    selected = int(input("Selected ::"))
    return selected


def vatCalculate(totalmoney):
    vat = 7
    result = totalmoney + (totalmoney * vat / 100)
    return result


def priceCalculate():
    price1 = int(input("First Product Price :"))
    price2 = int(input("Second Product Price :"))
    return vatCalculate(price1 + price2)


condition = True
while condition == True:
    if login() == True:
        showMenu()
        while True:
            selectedx = menuSelect()
            if selectedx == 1:
                totalmoney = int(input("Input Price :: "))
                print(vatCalculate(totalmoney))
                condition = False
                break
            elif selectedx == 2:
                print(priceCalculate())
                condition = False
                break
            else:
                print("Please check")
    else:
        print("Login Error Please check Username or password")
        continue
