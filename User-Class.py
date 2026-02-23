class User(AbstractUser):

    def __init__(self, user_id, name, email, password, phone):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__password = password   # Private - never exposed
        self.__phone = phone

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def verify_password(self, password):
        return self.__password == password   # Encapsulation: password stays private

    def get_profile(self):
        return (f"User ID: {self.__user_id} | Name: {self.__name} | "
                f"Email: {self.__email} | Phone: {self.__phone}")

    def get_role(self):
        return "Guest"

class Customer(User):
    
    def __init__(self, user_id, name, email, password, phone, address):
        super().__init__(user_id, name, email, password, phone)
        self.__address = address
        self.__order_history = []
        self.__cart = []

    def get_address(self):
        return self.__address

    def get_cart(self):
        return self.__cart

    def get_order_history(self):
        return self.__order_history

    def add_to_cart(self, product, quantity):
        self.__cart.append({"product": product, "quantity": quantity})
        print(f"  '{product.get_name()}' (x{quantity}) added to cart.")

    def clear_cart(self):
        self.__cart = []

    def add_order(self, order):
        self.__order_history.append(order)

    def get_role(self):
        return "Customer"

    def get_profile(self):
        base = super().get_profile()
        return f"{base} | Address: {self.__address} | Role: Customer"


class Admin(User):
    
    def __init__(self, user_id, name, email, password, phone, admin_level=1):
        super().__init__(user_id, name, email, password, phone)
        self.__admin_level = admin_level

    def get_admin_level(self):
        return self.__admin_level

    def get_role(self):
        return f"Admin (Level {self.__admin_level})"

    def get_profile(self):
        base = super().get_profile()
        return f"{base} | Role: Admin | Level: {self.__admin_level}"

