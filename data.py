arr_items = []

class items():
    def __init__(self, item, price):
        self.item = item
        self.price = price

def getAllItems():
    arr_items.clear()
    arr_items.append(items("susu", 50000))
    arr_items.append(items("daging", 20000))
    arr_items.append(items("lampu", 15000))
    arr_items.append(items("masker", 25000))
    arr_items.append(items("apel", 30000))
    return arr_items

def getPromoItems():
    arr_items.clear()
    arr_items.append(items("susu", 50000))
    arr_items.append(items("masker", 25000))
    return arr_items