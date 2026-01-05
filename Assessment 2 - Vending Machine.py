"ASSESSMENT 2 - Renee Aryan C. Roxas"
import time #lets us use pauses and loading effects


print("Welcome to Yakitate's Vending Machine!") 
print("---------------------------------------") 

#function that shows all items in a category
def show_items(items): 
    for code, (name, price, stock) in items.items():
        print(f"{code}.{name} - AED {price} (Stock: {stock})")
        
#Yakitate drink items (name, price, stock)
yakitate_drinks = {
    "D1": ("Milk Tea", 11,8),
    "D2": ("Matcha Latte", 8,8),
    "D3": ("Coffee", 6,8) ,
    "D4": ("Soda", 4,8)
                   }
#Yakitate snack items (name, price, stock)
yakitate_snacks = {
   "S1": ("Melon Pan", 12,8),
   "S2": ("Curry Bread", 15,8),
   "S3": ("Anpan", 8,8) ,
   "S4": ("Cheese Bread", 10,8)
                  }
#suggestions (each item suggests another item)
suggestions = {
    "D1" : "S1",
    "D2" : "S3",
    "D3" : "S4",
    "D4" : "S2",
    "S1" : "D1",
    "S2" : "D4",
    "S3" : "D2",
    "S4" : "D3",
    }

#combine all items so we can check codes easily
all_items = {**yakitate_drinks, **yakitate_snacks}

#loading animation for better user experience
def loading(message="Processing"):
    print(message, end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()
    
#makes sure the user enters a number (prevents errors)
def get_valid_money(prompt):
    while True:
        amount = input(prompt)
        try:
            return float(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")

def main(): 
    while True: #main loop of the vending machine
        print("\nMenu:")
        print("1. Drinks")
        print("2. Snacks")
        
        #shows all drink items
        print("\n--- Drinks ---")
        show_items(yakitate_drinks)
        
        #show all snack items
        print("\n--- Snacks ---")
        show_items(yakitate_snacks)
        
        #asks for item code (not case sensitive)
        item_code = input("\nEnter the item code: ").upper()
        
        #check if code exists
        if item_code not in all_items:
            print("\nInvalid item code. Please try again.")
            loading("Returning to menu")
            continue 
        
        #get item details
        name,price,stock = all_items[item_code]
        
        #check if item is in stock
        if stock == 0:
            print("Sorry, that item is out of stock.")
            continue
        
        #show price and ask for money
        print(f"{name} = AED {price}")
        money_inserted = get_valid_money("Insert money: ")
        
        #keeps asking for more money until it is enough
        while money_inserted < price: 
            print("Not enough money.")
            extra = get_valid_money("Insert more: ")
            money_inserted += extra
           
        #show loading while dispensing   
        loading(f"\nDispensing {name}...")
        print(f"{name} has been dispensed.")
        time.sleep(1.5)
        
        #calculate and show change
        loading("\nCalculating change")
        change = money_inserted - price 
        print(f"Your change is AED {change: .2f}")
        
        #reduce stock in all dictionaries
        all_items[item_code] = (name, price, stock - 1)
        if item_code.startswith("D"):
            yakitate_drinks[item_code] = (name, price, stock - 1)
        else:
            yakitate_snacks[item_code] = (name, price, stock - 1)
        
        #show suggestion if available
        if item_code in suggestions: 
            suggested_code = suggestions[item_code]
            suggested_name = all_items[suggested_code][0]
            print(f"\nYou might also like {suggested_name} ({suggested_code}).")
            
        #ask if user wants to buy again
        again = input("\nWould you like to buy again? (yes/no) ")
        
        if again == "no":
            print("\nThank you for using Yakitate's Vending Machine!")
            break

#call the function to start the program
main()
        

        
    