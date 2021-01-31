class Decimal(object):
    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __repr__(self):
        return "%.{}f".format(self.places) % self.number


class Currency(Decimal):
    def __init__(self, symbol, number, places):
        super().__init__(number, places)
        self.symbol = symbol

    def __repr__(self):
        # return "{}%.{}f".format(self.symbol, self.places) % self.number
        return "{}{}".format(self.symbol, super().__repr__())

    def add_currency(self, currency):
        # exchange between currencies
        pass


print(Decimal(15.6789, 3))
print(Currency("$", 15.6789, 3))
