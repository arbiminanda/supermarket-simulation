from data import getAllItems, getPromoItems
from messages import showActionsOptions, showWelcomingMessage
from command import printItems, printOrder

class order():
    def __init__(self, item, price, amount, total_price):
        self.item = item
        self.price = price
        self.amount = amount
        self.total_price = total_price
all_items = getAllItems()
promotional_items = getPromoItems()
finish_shop = False

showWelcomingMessage()
while not finish_shop:
    showActionsOptions()
    action_input = input("Input your answer here: ")
    if (action_input == "1"):
        print("Here are list of items that have special promo:")
        printItems(promotional_items)
    elif (action_input == "2"):
        print("Here are list of all items that you can buy:")
        printItems(all_items)
    elif (action_input == "3"):
        items_to_buy = []
        choose_items_done = False
        while not choose_items_done:
            print("Choose items that you want add to cart: (input number of desired item)")
            printItems(all_items)
            chosen_item = input("Input your option here: ")
            amount_item = input("How many do you want to buy that item? ")
            items_to_buy.append(order(all_items[int(chosen_item)-1].item, all_items[int(chosen_item)-1].price, amount_item, (all_items[int(chosen_item)-1].price)*int(amount_item)))
            print("Any other items do you want to buy? (Answer 'yes' or 'no')")
            finish_order = input("Your Answer: ")
            if (finish_order == "no"):
                i=0
                order_price = 0  
                while i<len(items_to_buy):
                    order_price += items_to_buy[i].total_price
                    i += 1
                print("Total Price of your order: Rp." + str(order_price))
                print("Here are your order detail:")
                printOrder(items_to_buy)
                print("Thanks for buying our items ^_^")
                choose_items_done = True
    else:
        print("Thanks for coming, have a nice day ^_^")
        finish_shop = True