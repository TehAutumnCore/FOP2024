class SalesForDay:

    def __init__(self,number_of_days_open,sales_dict):
        self._number_of_days_open = number_of_days_open
        self._sales_dict = sales_dict #keys = name of item sold; vale = # of items sold
    
    def get_day(self):
        return self._number_of_days_open

    def get_sales_dict(self):
        return self._sales_dict