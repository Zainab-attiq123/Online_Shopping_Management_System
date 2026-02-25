class Product(AbstractProduct):

    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    # Getters
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative!")
        else:
            self.__price = price

    def get_details(self):
        return f"[{self.__product_id}] {self.__name} - Rs.{self.__price}"
