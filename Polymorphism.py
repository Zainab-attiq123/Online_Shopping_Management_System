class PaymentProcessor:
   
    @staticmethod
    def process_payment(payment_method, amount):
        return payment_method.pay(amount)


class CashPayment:
    def pay(self, amount):
        print(f"  Cash Payment of Rs.{amount:.2f} received at delivery.")
        return True


class CardPayment:
    def __init__(self, card_number, holder_name):
        self.__card_number = f"****-****-****-{card_number[-4:]}"
        self.__holder = holder_name

    def pay(self, amount):
        print(f"  Card Payment of Rs.{amount:.2f} charged to {self.__card_number} ({self.__holder}).")
        return True


class EasyPaisaPayment:
    def __init__(self, mobile_number):
        self.__mobile = mobile_number

    def pay(self, amount):
        print(f"  EasyPaisa Payment of Rs.{amount:.2f} sent from {self.__mobile}.")
        return True


class JazzCashPayment:
    def __init__(self, mobile_number):
        self.__mobile = mobile_number

    def pay(self, amount):
        print(f"  JazzCash Payment of Rs.{amount:.2f} sent from {self.__mobile}.")
        return True


# Polymorphism also in display:
def display_product_info(product):
    
    print(f"  Category : {product.get_category()}")
    print(f"  Details  : {product.get_details()}")

