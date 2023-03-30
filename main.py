from data import getAllItems, getPromoItems
from messages import showActionsOptions, showWelcomingMessage
from functions import printItems, printOrder, handleOrder, calculateTotalOrderPrice

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
        items_to_buy = handleOrder(all_items)
        print("Total Price of your order: Rp." + str(calculateTotalOrderPrice(items_to_buy)))
        print("Here are your order detail:")
        printOrder(items_to_buy)
        print("Thanks for buying our items ^_^")
    elif (action_input == "4"):
        print("Thanks for coming, have a nice day ^_^")
        finish_shop = True
    else:
        print("Sorry, Error input")
        break