price = 0 
chicken = 5.25
beef = 6.25
tofu = 5.75
smalldrink = 1.00
mediumdrink = 1.75
largedrink = 2.25
smallfry = 1.00 
mediumfry = 1.50
largefry = 2.00
ketchup = 0.25
finalorder = []
def menu():
    print("Chicken Sandwich: $" + str(chicken))
    print("Beef Sandwhich: $" + str(beef))
    print("Tofu Sandwich: $" + str(tofu))
def drinksize():
    print("Small: $1.00")
    print("Medium: $1.75")
    print("Large: $2.25")
def frysizeselec ():
    print("Small: $1.00")
    print("Medium: $1.50")
    print("Large: $2.00")
def ketchupprice ():
    print("1 Ketchup Packet: $0.25")
menu()


#iteration 1 SANDWICH
while 1 == 1:
    sandwich = input("What type of Sandwhich do you want?")
    sandwichamo = int(input("How many sandwiches do you want?"))
    if sandwich == "chicken":
        price = price + chicken * sandwichamo
        finalorder.append("Chicken Sandwich: " + str(sandwichamo))
        break
    if sandwich == "beef":
        price = price + beef * sandwichamo 
        finalorder.append("Beef Sandwich: " + str(sandwichamo))
        break
    if sandwich == "tofu":
        finalorder.append("Tofu Sandwich: " + str(sandwichamo))
        price = price + tofu * sandwichamo
        break
    if sandwich == "n":
        finalorder.append("No sandwich")
        break 
    if sandwich != ["chicken", "beef", "tofu"]:
        print("Please choose one of the three sandwiches above. If you do not want a sandwich, type 'n'. ")
        print()
if sandwich == "n":
    print("You have chosen not to get a sandwich.")
else: 
    print("You have selected " + str(sandwichamo) + " " + str(sandwich) + " sandwich(es).")
print()


#iteration 2 DRINKS
drink = input("Would you like a beverage? y/n: ")
if drink == "y":
    drinksize()
    drinkselec = input("What drink size would you like?")
    drinkamo = int(input("How many drinks would you like?"))
    if drinkselec == "small":
        print("You have selected " + str(drinkamo) + " small drink(s).")
        finalorder.append("Drink: Small: " + str(drinkamo))
        price = price + smalldrink * drinkamo 
    if drinkselec == "medium":
        print("You have selected " + str(drinkamo) + " medium drink(s).")
        finalorder.append("Drink: Medium: " + str(drinkamo))
        price = price + mediumdrink * drinkamo
    if drinkselec =="large":
        print("You have selected " + str(drinkamo) + " large drink(s).")
        finalorder.append("Drink: Large " + str(drinkamo))
        price = price + largedrink * drinkamo
elif drink == "n":
    print("You have chosen not to get a drink.")
    finalorder.append("No drink.")
print()


#iteration 3 FRIES
fryselec = input("Would you like french fries? y/n: ")
if fryselec == "y":
    frysizeselec()
    frysize = input("What size of fries would you like?")
    fryamo = int(input("How many fries would you like?"))
    if frysize == "small":
        print("You have selected " + str(fryamo) + " small fries.")
        finalorder.append("Fries: Small: " + str(fryamo))
        price = price + smallfry * fryamo
    if frysize == "medium":
        print("You have selected " + str(fryamo) + " medium fries.")
        finalorder.append("Fries: Medium: " + str(fryamo))
        price = price + mediumfry * fryamo
    if frysize == "large":
        print("You have selected " + str(fryamo) + " large fries.")
        finalorder.append("Fries: Large: " + str(fryamo))
        price = price + largefry * fryamo
if fryselec == "n":
    print("You have chosen not to get fries.")
    finalorder.append("No fries.")
print()


#iteration 4 KETCHUP
ketchupprice()
ketchupselec = input("Would you like to buy ketchup packets? y/n: ")
while 1 == 1:
    if ketchupselec == "y":
            ketchupamo = int(input("How many ketchup packets do you want?"))
            if ketchupamo <= 0:
                print("Please input a valid amount of packets.")
            else:
                ketchup = ketchupamo * ketchup 
                price = price + ketchup 
                print("You have selected to buy " + str(ketchupamo) + (" ketchup packets."))
                finalorder.append("Ketchup Packets: " + str(ketchupamo))
                break
    if ketchupselec == "n":
        print("You have chosen to not buy ketchup packets.")
        finalorder.append("No ketchup packets")
        break
print()


#final order
print("Full Order:")
print(finalorder)
print("Total price: $" + str(price))