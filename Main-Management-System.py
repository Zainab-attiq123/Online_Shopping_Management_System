class ShoppingManagementSystem:
   
    def __init__(self, brand_name):
        self.__brand_name = brand_name
        self.__inventory = {}
        self.__customers = {}
        self.__admins = {}
        self.__orders = {}

    def add_product(self, product):
        self.__inventory[product.get_product_id()] = product
        print(f"  + Product '{product.get_name()}' added to inventory.")

    def register_customer(self, customer):
        self.__customers[customer.get_user_id()] = customer
        print(f"  + Customer '{customer.get_name()}' registered.")

    def register_admin(self, admin):
        self.__admins[admin.get_user_id()] = admin
        print(f"  + Admin '{admin.get_name()}' registered.")

    def get_product(self, product_id):
        return self.__inventory.get(product_id)

    def get_customer(self, user_id):
        return self.__customers.get(user_id)

    def place_order(self, customer, payment_method):
        cart = customer.get_cart()
        if not cart:
            print("  Cart is empty!")
            return None

        for item in cart:
            p = item["product"]
            if p.get_stock() < item["quantity"]:
                print(f"  Insufficient stock for '{p.get_name()}'!")
                return None

        order = Order(customer, list(cart))

        print(f"\n  Processing payment of Rs.{order.get_total():.2f}...")
        success = PaymentProcessor.process_payment(payment_method, order.get_total())

        if success:
            for item in cart:
                item["product"].reduce_stock(item["quantity"])
            customer.add_order(order)
            customer.clear_cart()
            self.__orders[order.get_order_id()] = order
            order.update_status("Confirmed")
            print(f"  Order placed successfully! Order ID: {order.get_order_id()}")
            return order
        else:
            print("  Payment failed!")
            return None

    def show_inventory(self, gender_filter=None):
        print(f"\n  {'='*65}")
        title = f"INVENTORY" + (f" - {gender_filter}" if gender_filter else " - ALL")
        print(f"  {title:^65}")
        print(f"  {'='*65}")
        found = False
        for pid, product in self.__inventory.items():
            if gender_filter is None or product.get_gender() == gender_filter or product.get_gender() == "Unisex":
                print(f"\n  {product.get_details()}")
                found = True
        if not found:
            print("  No products found.")
        print(f"  {'='*65}")

    def apply_sale(self, gender, discount_pct):
        print(f"\n  Applying {discount_pct}% sale on all {gender} items...")
        for product in self.__inventory.values():
            if product.get_gender() == gender or gender == "All":
                product.apply_discount(discount_pct)

    def show_all_orders(self):
        if not self.__orders:
            print("  No orders found.")
            return
        for order in self.__orders.values():
            print(order.get_summary())


