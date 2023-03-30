from data import getAllItems, getPromoItems
from messages import showActionsOptions, showWelcomingMessage
from command import printItems

all_items = getAllItems()
promotional_items = getPromoItems()
finish_order = False

showWelcomingMessage()
while not finish_order:
    showActionsOptions()
    action_input = input()
    if (action_input == "1"):
        print("Here are list of items that have special promo:")
        printItems(promotional_items)
    elif (action_input == "2"):
        print("Here are list of all items that you can buy:")
        printItems(all_items)
    elif (action_input == "3"):
        print("Buy Items")
    else:
        print("Thanks for coming, have a nice day ^_^")
        break