class Coffee:
    state = ""

    def __init__(self, water, milk, beans, cups, money):
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.water = water

    def states(self):
        print("Write action (buy, fill, take, remaining, exit):")
        self.state = input()
        while self.state != "exit":
            try:
                if self.state == "buy":
                    purchase = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to "
                                     "main menu:")
                    if purchase == "1":
                        if self.beans >= 16 and self.water >= 250 and self.cups >= 1:
                            print("I have enough resources, making you a coffee!")
                            self.money += 4
                            self.beans -= 16
                            self.water -= 250
                            self.cups -= 1
                        elif self.beans < 16:
                            print("Sorry, not enough beans!")
                        elif self.water < 250:
                            print("Sorry, not enough water!")
                        elif self.cups < 1:
                            print("Sorry, not enough cups!")
                    elif purchase == "2":
                        if self.beans >= 7 and self.water >= 250 and self.milk >= 75 and self.cups >= 1:
                            print("I have enough resources, making you a coffee!")
                            self.money += 7
                            self.water -= 350
                            self.milk -= 75
                            self.beans -= 20
                            self.cups -= 1
                        elif self.beans < 16:
                            print("Sorry, not enough beans!")
                        elif self.water < 250:
                            print("Sorry, not enough water!")
                        elif self.cups < 1:
                            print("Sorry, not enough cups!")
                        elif self.milk < 75:
                            print("Sorry, not enough milk!")
                    elif purchase == "3":
                        if self.beans >= 12 and self.water >= 200 and self.milk >= 100 and self.cups >= 1:
                            print("I have enough resources, making you a coffee!")
                            self.money += 6
                            self.water -= 200
                            self.milk -= 100
                            self.beans -= 12
                            self.cups -= 1
                        elif self.beans < 12:
                            print("Sorry, not enough beans!")
                        elif self.water < 200:
                            print("Sorry, not enough water!")
                        elif self.cups < 1:
                            print("Sorry, not enough cups!")
                        elif self.milk < 100:
                            print("Sorry, not enough milk!")
                    elif purchase == "back":
                        break
                elif self.state == "fill":
                    self.water += int(input("Write how many ml of water do you want to add:"))
                    self.milk += int(input("Write how many ml of milk do you want to add:"))
                    self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
                    self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
                elif self.state == "take":
                    print(f"I gave you ${self.money}")
                    self.money = 0
                elif self.state == "remaining":
                    print(f"""
                       The coffee machine has:
                       {self.water} of water
                       {self.milk} of milk
                       {self.beans} of beans
                       {self.cups} of disposable cups
                       ${self.money} of money """)
                dad = input()
                self.state = dad
            except EOFError:
                break
Machine = Coffee(400,540,120,9,550)
Machine.states()