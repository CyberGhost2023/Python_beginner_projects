money_in_machine = 550
water_in_machine = 400
milk_in_machine = 540
beans_in_machine = 120
cups_in_machine = 9


def current_status():
    current = """The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money""".format(water_in_machine,
                      milk_in_machine,
                      beans_in_machine,
                      cups_in_machine,
                      money_in_machine)
    print(current)
	
	
def buy():
    global money_in_machine, water_in_machine, milk_in_machine, beans_in_machine, cups_in_machine
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    option = input()
    flag = 0
    if option == "1":
        if water_in_machine < 250:
            flag = 1
        elif beans_in_machine < 16:
            flag = 3
        elif cups_in_machine < 1:
            flag = 4
        else:    
            water_in_machine -= 250
            beans_in_machine -= 16
            money_in_machine += 4
            flag = 5
    elif option == "2":
        if water_in_machine < 350:
            flag = 1
        elif milk_in_machine < 75:
            flag = 2
        elif beans_in_machine < 20:
            flag = 3
        elif cups_in_machine < 1:
            flag = 4
        else:
            water_in_machine -= 350
            milk_in_machine -= 75
            beans_in_machine -= 20
            money_in_machine += 7
            flag = 5
    elif option == "3":
        if water_in_machine < 200:
            flag = 1
        elif milk_in_machine < 100:
            flag = 2
        elif beans_in_machine < 12:
            flag = 3
        elif cups_in_machine < 1:
            flag = 4
        else:
            water_in_machine -= 200
            milk_in_machine -= 100
            beans_in_machine -= 12
            money_in_machine += 6
            flag = 5
    if flag == 5:
        print("I have enough resources, making you a coffee!")
        cups_in_machine-= 1
    elif flag == 1:
        print("Sorry, not enough water!")
    elif flag == 2:
        print("Sorry, not enough milk!")
    elif flag == 3:
        print("Sorry, not enough coffee beans!")
    elif flag == 4:
        print("Sorry, not enough cups!")
	

def fill():
    global money_in_machine, water_in_machine, milk_in_machine, beans_in_machine, cups_in_machine
    added_water = int(input("Write how many ml of water do you want to add:\n "))
    added_milk = int(input("Write how many ml of milk do you want to add:\n "))
    added_beans = int(input("Write how many grams of coffee beans do you want to add:\n "))
    added_cups = int(input("Write how many disposable cups of coffee do you want to add:\n "))
    water_in_machine += added_water
    milk_in_machine += added_milk
    beans_in_machine += added_beans
    cups_in_machine += added_cups


def take():
    global money_in_machine
    print("I gave you ${}".format(money_in_machine))
    money_in_machine = 0

while 1:
    action = input("Write action (buy, fill, take, remaining, exit):\n ")
    if action == "exit":
        break
    elif action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        current_status()
	
