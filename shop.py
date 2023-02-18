from colorama import Fore, Back, Style

class Shop:
    def __init__(self, name, isAdmin):
        self.inventory = {"Book": 1.00, "Cake": 2.00, "Cookies":1.50}
        self.name = name
        self.isAdmin = isAdmin
        self.basket = {}
        self.total = 0
    
    def update_basket(self, item, quantity):
        if item.capitalize() in self.inventory.keys():
            print(f"\n{quantity} {item.capitalize()} added to the basket")
            price = self.inventory[item.capitalize()] 
            subtotal = price * float(quantity)
            self.basket[item.capitalize()] = {"price":price, "quantity":quantity, "subtotal":subtotal}
            self.total += subtotal
        else:
            print("\nItem does not exist")

    def add_to_inventory(self, item, price):
        if item.isalpha():
            self.inventory[item.capitalize()] = float(price)
            print(Fore.GREEN+f"\n\t{item} added to inventory successfully\n")
        else:
            print(Fore.RED+"\n\tEnter only numbers for the price and only letters for items\n"+Fore.WHITE)

    
    def remove_from_inventory(self, item):
        if item.capitalize() not in self.inventory.keys():
            return -1
        del self.inventory[item.capitalize()]
        return 0

    def print_basket(self):
        print(Fore.MAGENTA+"---- Your basket ----\n".center(45) +Fore.WHITE)
        if self.basket:
            for i, j in self.basket.items():
                print(Fore.BLUE + f"{i}".center(43)+ Fore.WHITE)
                for k, l in j.items():
                    if k == "price" or k == "subtotal":
                        print(f"\t{k:<22}: "+Fore.CYAN+f"£{l:.2f}"+Fore.WHITE)  
                    else:  
                        print(f"\t{k:<22}: "+Fore.CYAN+f"{l:<5}"+Fore.WHITE)    
                print("")
            print(Fore.BLUE+("Total:"+Fore.GREEN+f" £{self.total:.2f}\n").center(48)+Fore.WHITE)
    
    def print_inventory(self):
        print("\nHere is our inventory:")
        print(Fore.CYAN)
        for i, j in self.inventory.items():
            print(f"\t{i}: £{j:.2f}")
        print(Fore.WHITE)

    def print_options(self):
        options = {1:"Continue shopping", 2:"Checkout", 3:"View basket"}
        admin_options = {4:"Add items to inventory", 5:"Remove items from inventory"}
        print(Fore.MAGENTA+f"---- Navigation ----\n".center(45))
        print((Fore.WHITE + "Type "+Fore.RED+"quit"+Fore.WHITE+" to exit the program\n").center(60))

        for key, option in options.items():
            print(Fore.GREEN+f"{key:>12}) {option}")

        print("")
        print(Fore.RED+"---- ADMINS ONLY ----".center(43))
        for key, option in admin_options.items():
            print(f"{key:>12}) {option}")

    def accept_option(self):
        while True:
            selected = input(Fore.WHITE+"Enter number for the corresponding option: "+Fore.BLUE)
            if selected.upper() == "QUIT":
                return 0
            elif selected == "1":
                return 1
            elif selected == "2":
                return 2
            elif selected == "3":
                return 3
            elif selected == "4":
                return 4
            elif selected == "5":
                return 5
            self.print_options()
            print(Fore.RED+"Invalid option selected\n\nPlease select a number from the menu above.\n")
    
    def checkout(self):
        self.print_basket()
        print("Thank you for shopping with us.")
