from shop import Shop, Fore, Style
print(Style.BRIGHT)
customer_name = input(Fore.WHITE+"Welcome what is your name? "+Fore.BLUE)
while True:
    print(Fore.WHITE)
    isAdmin = input("Are you an admin? ( Y | N ) "+ Fore.BLUE )
    print(Fore.WHITE)
    if isAdmin.upper() == "N":
        break
    if isAdmin.upper() == "Y":
        password = input("Enter your password to continue: "+Fore.BLUE)
        if password == "anwar":
            print(Fore.WHITE)
            break
        else:
            print(Fore.RED+"\nIncorrect password!")
customer = Shop(customer_name, True if isAdmin.upper() == "Y" else False)
    

while True:
    customer.print_options()
    print(Fore.WHITE)
    selected_option = customer.accept_option()
    print(Fore.WHITE)
    if selected_option == 0:
        print(Fore.GREEN+"\nThanks for visiting. We hope to see you soon\n"+ Fore.WHITE)
        break
    if selected_option == 1:
        customer.print_inventory()
        while True:
            customer_choice = input(Fore.WHITE+"\nSelect the item and the quantity of items you would like to purchase:\nEnter "+ Fore.RED +"quit"+Fore.WHITE+" to exit.\n\n>>> "+ Fore.BLUE)
            if customer_choice.upper() == "QUIT":
                break
            try:
                item, quantity = customer_choice.split(" ")
                if item.isdigit() or quantity.isalpha() or not quantity:
                    print(Fore.RED+"\nPlease enter the item you would like to buy followed by a space then the quantity like so:"+Fore.GREEN+"\n\n cake 4\n"+Fore.WHITE)
                    continue
                customer.update_basket(item, quantity)
            except ValueError:
                print(Fore.RED+"\nPlease enter the item you would like to buy followed by a space then the quantity like so:"+Fore.GREEN+"\n\n cake 4\n"+Fore.WHITE)
    if selected_option == 2:
        customer.checkout()
        break
    if selected_option == 3:
        customer.print_basket()
    if selected_option == 4:
        if not customer.isAdmin:
            print(Fore.RED+"\n\t----- Unauthorised access! -----\n")
        else:
            while True:
                try:
                    new_item = input("What is the item you would like to add? "+Fore.BLUE)
                    price = float(input(Fore.WHITE+"What is the price of the item you would like to add? "+Fore.BLUE))
                    print(Fore.WHITE)
                    customer.add_to_inventory(new_item, price)
                    break
                except ValueError:
                    print(Fore.RED+"\n\tEnter only numbers for the price and only letters for items\n"+Fore.WHITE)
    if selected_option == 5:
        if not customer.isAdmin:
            print(Fore.RED+"\n\t----- Unauthorised access! -----\n")
        else:
            while True:
                del_item = input("What is the item you would like to delete? "+Fore.BLUE)
                if del_item.lower() == "quit":
                    break
                if customer.remove_from_inventory(del_item) < 0:
                    print(Fore.RED+f"\nCouldn't find {del_item} in inventory.\nEnter quit to exit."+Fore.WHITE)
                else:
                    print(Fore.GREEN+f"\n{del_item} successfully deleted\n"+Fore.WHITE)
                    break





        
