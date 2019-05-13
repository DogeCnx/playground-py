usernameinput = input("Username ::")
passwordinput = input("Password ::")
if usernameinput == "Doge" and passwordinput == "wow":
    print("Welcome to Doge Weapon")
    print("----------------------")
    print("1 AK-47 x1  1000 THB")
    print("2 M4A1  x1  2500 THB")
    print("3 RPG-7 x1  3000 THB")
    userSelected = int(input(">>"))
    if userSelected == 1:
        weaponNeedAK = int(input("Number of weapon needed ::"))
        print(":: Doge Weapon :: ")
        print("------------------")
        print("AK-47   x", weaponNeedAK, "1000THB")
        print("------------------")
        print("Total", weaponNeedAK*1000, "THB")
    elif userSelected == 2:
        weaponNeedM4 = int(input("Number of weapon needed ::"))
        print(":: Doge Weapon :: ")
        print("------------------")
        print("M4A1   x", weaponNeedM4, "2500THB")
        print("------------------")
        print("Total", weaponNeedM4*2500, "THB")
    elif userSelected == 3:
        weaponNeedRPG = int(input("Number of weapon needed ::"))
        print(":: Doge Weapon :: ")
        print("------------------")
        print("RPG   x", weaponNeedRPG, "3000THB")
        print("------------------")
        print("Total", weaponNeedRPG*3500, "THB")
    else:
        print("Error select")
else:
    print("Username or Password is incorrect ")