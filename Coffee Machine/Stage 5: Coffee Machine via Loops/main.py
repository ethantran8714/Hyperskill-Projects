def menu(water,milk,beans,cups,money):
    print(f"""
    The coffee machine has: 
    {water} of water
    {milk} of milk
    {beans} of beans
    {cups} of disposable cups
    ${money} of money """)

def main():
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    while water >= 0 and milk >= 0 and beans >= 0 and cups >= 0:
        action = input("Write action (buy,fill,take,remaining,exit):")
        if action == "buy":
            purchase = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:")
            if (water <= 200 and water > 0) or milk < 75 or beans < 12 or cups < 1:
                print("Sorry, not enough water!")
                continue
            if purchase == "1":
                if water >= 250 and beans >= 16 and cups >= 1:
                    print("I have enough resources, making you a coffee!")
                money += 4
                beans -= 16
                water -= 250
                cups -= 1
            elif purchase == "2":
                if water >= 350 and milk >= 75 and beans >= 20 and cups > 1:
                    print("I have enough resources, making you a coffee!")
                money += 7
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
            elif purchase == "3":
                if water >= 200 and milk >= 100 and beans >= 12:
                    print("I have enough resources, making you a coffee!")
                money += 6
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
            elif purchase == "back":
                continue
        elif action == "fill":
            water += int(input("Write how many ml of water do you want to add:"))
            milk += int(input("Write how many ml of milk do you want to add:"))
            beans += int(input("Write how many grams of coffee beans do you want to add:"))
            cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        elif action == "take":
            print(f"I gave you ${money}")
            money = 0
        elif action == "remaining":
            menu(water, milk, beans, cups, money)
        elif action == "exit":
            break

main()

