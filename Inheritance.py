class Clothing(Product):

    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.__size = size

    def get_details(self):
        return f"{super().get_details()} | Size: {self.__size}"


class User(AbstractUser):

    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name

    def get_profile(self):
        return f"User ID: {self.__user_id} | Name: {self.__name}"


class Customer(User):

    def get_profile(self):
        return super().get_profile() + " | Role: Customer"


class Admin(User):

    def get_profile(self):
        return super().get_profile() + " | Role: Admin"
