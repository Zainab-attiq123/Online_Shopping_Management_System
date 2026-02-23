class Product(AbstractProduct):
    
    def __init__(self, product_id, name, price, stock, gender, size, color):
        # Private attributes (name mangling with __)
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__gender = gender   # 'Male', 'Female', 'Unisex'
        self.__size = size       # XS, S, M, L, XL, XXL
        self.__color = color

    # --- Getters (Encapsulation) ---
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def get_gender(self):
        return self.__gender

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    # --- Setters with Validation (Encapsulation) ---
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = price

    def set_stock(self, stock):
        if stock < 0:
            raise ValueError("Stock cannot be negative!")
        self.__stock = stock

    def reduce_stock(self, quantity):
        if quantity > self.__stock:
            raise ValueError(f"Insufficient stock! Available: {self.__stock}")
        self.__stock -= quantity

    # Abstract method implementations
    def get_details(self):
        return (f"[ID: {self.__product_id}] {self.__name} | "
                f"Price: Rs.{self.__price:.2f} | Size: {self.__size} | "
                f"Color: {self.__color} | Gender: {self.__gender} | "
                f"Stock: {self.__stock}")

    def apply_discount(self, percentage):
        if 0 < percentage <= 100:
            discounted = self.__price - (self.__price * percentage / 100)
            self.__price = round(discounted, 2)
            return self.__price
        raise ValueError("Discount must be between 1 and 100!")

    def get_category(self):
        return "General Clothing"

    def __str__(self):
        return self.get_details()

