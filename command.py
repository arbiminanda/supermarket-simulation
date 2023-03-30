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