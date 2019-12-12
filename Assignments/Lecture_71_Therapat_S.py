import math


def showBill():
    print("MyFoodDOOGE".center(30, "-"))
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
    print("Total Price Food :: ", sum(priceList))


menuList = []
priceList = []

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
