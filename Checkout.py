class Checkout:

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = []
    def addItemPrice(self, item, price):
        self.prices[item] = price
    def addItem(self, item):
        self.items.append(item)
    def calculateTotal(self):
        total = 0
        for item in self.items:
            total += self.prices[item]
        return total
    def addDiscount(self, item, num, price):
        self.discounts[item, num] = price