class MenuItem:
    def __init__(self,name,wholesale_cost_float,selling_price_float):
        print("Hello, world")
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        return self._name #a string for the item's name
        
    def get_wholesale_cost(self):
        return self._wholesale_cost #a float for the item's wholesale cost (how much the stand pays for the item)
        
    def get_selling_price(self):
        return self._selling_price #a float for the item's selling price (how much the stand sells the item for)