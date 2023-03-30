def printItems(arr_items):
    i=0
    while i<len(arr_items):
        print(str(i+1) + ". Item Name: " + (arr_items[i].item).capitalize() + ", Price: " + str(arr_items[i].price))
        i += 1