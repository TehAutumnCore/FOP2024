# class MenuItem:
#     def __init__(self,name,wholesale_cost_float,selling_price_float):
#         print("Hello, world")
#         self._name = name
#         self._wholesale_cost_float = wholesale_cost_float
#         self._selling_price_float = selling_price_float

#     def get_name(self):
#         return self.name #a string for the item's name
    
#     def get_wholesale_cost(self):
#         return self.wholesale_cost_float#a float for the item's wholesale cost (how much the stand pays for the item)
    
#     def get_selling_price(self):
#         return self.selling_price_float#a float for the item's selling price (how much the stand sells the item for)

# class SalesForDay:
#     def __init(self,number_of_days,sales_dictionary):
#         self.number_of_days = 0 #an integer for the number of days the stand has been open so far
#         self.sales_dictionary = {}#a dictionary whose keys are the names of the items sold and whose values are the numbers of those items sold that day
    
#     def get_day(self): 
#         return self.number_of_days
    
#     def get_sales_dict(self):
#         return self.sales_dictionary

# class LemonadeStand:
#     def __init__ (self,name_of_stand):
#         self._name_of_stand = name_of_stand

#     def get_name(self):
#         return name_of_stand

#     def add_menu_item(self,MenuItem_object):
#         Menu_Dict += MenuItem_object

#     def enter_sales_for_today(self,dictionary_of_items_sold_and_how_many_sold):
#         dictionary_of_items_sold_and_how_many_sold = {} #key = name of items sold : value = how many of the item sold

from sales_for_day import SalesForDay
from menu_item import MenuItem
class InvalidSalesItemError(Exception):
    pass

class LemonadeStand:
    def __init__(self,name_of_stand):
        self._name_of_stand = name_of_stand
        self._current_day = 0
        self._menu = {} #keys: ;values:
        self._sales_record = [] #list of SalesForDay objects
    
    def get_name(self):
        return self._name_of_stand

    def add_menu_item(self,menu_item_object):
        self._menu[menu_item_object.get_name()] = menu_item_object
    
    def enter_sales_for_today(self,item_sold_dict):
        # day_0_sales = {'lemonade': 5, 'cookie': 2}
        for items in item_sold_dict.keys():
            if items not in self._menu:
                raise InvalidSalesItemError(f"The item {items} is not on our menu")
        new_sales_for_day_obj = SalesForDay(self._current_day,item_sold_dict)
        self._sales_record.append(new_sales_for_day_obj)
        self._current_day += 1

    def sales_of_menu_item_for_day(self,day,name_of_menu_item):
        for sales in self._sales_record:
            if day == sales.get_day():
                sales_log = sales.get_sales_dict()
                if name_of_menu_item in sales_log:
                    return sales_log[name_of_menu_item] #.get() is a method to grab an item from a dict, also can pass 2nd arguement
                else:
                    return 0 
        return "No information found for that day"
    
    def total_sales_for_menu_item(self,name_of_menu_item):
        total_sales = 0
        for sales in self._sales_record:
            day = sales.get_day()
            sales_for_day = self.sales_of_menu_item_for_day(day,name_of_menu_item)
            total_sales += sales_for_day
        return total_sales
    
    def total_profit_for_menu_item(self,name_of_menu_item):
        total_sales = self.total_sales_for_menu_item(name_of_menu_item)
        menu_object = self._menu[name_of_menu_item]
        profit = menu_object.get_selling_price() - menu_object.get_wholesale_cost()
        return profit * total_sales

    def total_profit_for_stand(self):
        total_profit = 0
        for menu_item in self._menu.keys():
            total_profit += self.total_profit_for_menu_item(menu_item)
        return total_profit

def main():
    stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
    item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
    item2 = MenuItem(('nori'), 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
    item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

    # This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
    day_0_sales = {
        'lemonade' : 5,
        'cookie'   : 2
    }

    stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")  # print the total profit for lemonade so far

if __name__ = "__main__":
    main()