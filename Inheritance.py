class MaleClothing(Product):

    def __init__(self, product_id, name, price, stock, size, color, clothing_type):
        super().__init__(product_id, name, price, stock, "Male", size, color)
        self.__clothing_type = clothing_type  # Shirt, Trouser, Kurta, Jacket, etc.

    def get_clothing_type(self):
        return self.__clothing_type

    def get_category(self):
        return f"Male Clothing - {self.__clothing_type}"

    def get_details(self):
        base = super().get_details()
        return f"{base} | Type: {self.__clothing_type}"

    def apply_discount(self, percentage):
        new_price = super().apply_discount(percentage)
        print(f"  Male clothing discount applied! New price: Rs.{new_price:.2f}")
        return new_price


class FemaleClothing(Product):

    def __init__(self, product_id, name, price, stock, size, color, clothing_type, style="Casual"):
        super().__init__(product_id, name, price, stock, "Female", size, color)
        self.__clothing_type = clothing_type  # Kurti, Dress, Lehenga, Shalwar, etc.
        self.__style = style                  # Casual, Formal, Party, Traditional

    def get_clothing_type(self):
        return self.__clothing_type

    def get_style(self):
        return self.__style

    def get_category(self):
        return f"Female Clothing - {self.__clothing_type}"

    def get_details(self):
        base = super().get_details()
        return f"{base} | Type: {self.__clothing_type} | Style: {self.__style}"

    def apply_discount(self, percentage):
        new_price = super().apply_discount(percentage)
        print(f"  Female clothing discount applied! New price: Rs.{new_price:.2f}")
        return new_price


class UnisexClothing(Product):
    
    def __init__(self, product_id, name, price, stock, size, color, clothing_type):
        super().__init__(product_id, name, price, stock, "Unisex", size, color)
        self.__clothing_type = clothing_type

    def get_clothing_type(self):
        return self.__clothing_type

    def get_category(self):
        return f"Unisex Clothing - {self.__clothing_type}"

    def get_details(self):
        base = super().get_details()
        return f"{base} | Type: {self.__clothing_type}"

    def apply_discount(self, percentage):
        new_price = super().apply_discount(percentage)
        print(f"  Unisex clothing discount applied! New price: Rs.{new_price:.2f}")
        return new_price


