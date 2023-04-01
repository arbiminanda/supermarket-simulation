import sys

class order():
    def __init__(self, item, price, amount, total_price):
        self.item = item
        self.price = price
        self.amount = amount
        self.total_price = total_price

def handleOrder(arr_items):
    choose_items_done = False
    orders = []
    while not choose_items_done:
        print("Choose items that you want add to cart: (input number of desired item)")
        printItems(arr_items)
        chosen_item = input("Input your option here: ")
        while int(chosen_item) not in range(1,len(arr_items)+1):
            print("Sorry, please give a correct input")
            chosen_item = input("Input your option here: ")
        amount_item = input("How many do you want to buy that item? ")
        orders.append(order(arr_items[int(chosen_item)-1].item, arr_items[int(chosen_item)-1].price, amount_item, (arr_items[int(chosen_item)-1].price)*int(amount_item)))
        print("Any other items do you want to buy? (Answer 'y' for yes or 'n' for no)")
        finish_order = input("Your Answer: ")
        while (finish_order not in ["y", "n"]):
            print("Sorry, please give a correct input")
            finish_order = input("Your Answer: ")
        if (finish_order == "n"):
            choose_items_done = True
        elif (finish_order == "y"):
            choose_items_done = False
    return orders

def printItems(arr_items):
    i=0
    while i<len(arr_items):
        print(str(i+1) + ". Item Name: " + (arr_items[i].item).capitalize() + ", Price: Rp." + str(arr_items[i].price))
        i += 1

def printOrder(arr_items):
    i=0
    while i<len(arr_items):
        print(str(i+1) + ". Item Name: " + (arr_items[i].item).capitalize() + ", Price: Rp." + str(arr_items[i].price) + ", Amount: " + str(arr_items[i].amount) + ", Total Price: Rp." + str(arr_items[i].total_price))
        i += 1

def calculateTotalOrderPrice(arr_orders):
    i=0
    total_price = 0  
    while i<len(arr_orders):
        total_price += arr_orders[i].total_price
        i += 1
    return total_price