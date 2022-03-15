class Checkout:
    class Discount:
        def __init__(self, itemName, numOfItems, price):
            self.numOfItems = numOfItems
            self.price = price
            self.itemName = itemName

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = []
    def addItemPrice(self, item, price):
        self.prices[item] = price
    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        self.items.append(item)

    def countItems(self):
        count = {}
        for item in self.items:
            if item in count:
                count[item]+=1
            else:
                count[item]=1
        return count

    def calculateTotal(self):
        count = self.countItems()
        total = 0
        for key in self.discounts:
            discount = self.discounts[key]
            if discount.itemName in count:
                while count[discount.itemName] >= discount.numOfItems:
                    count[discount.itemName] -= discount.numOfItems
                    total += discount.price

        for item in count:
            total += self.prices[item] * count[item]

        return total


    def addDiscount(self, item, num, price):
        discount = self.Discount(item, num, price)
        self.discounts[item] = discount
