
class Order:
    
    order_counter = 1000  # Class variable

    def __init__(self, customer, items):
        self.__order_id = f"ORD-{Order.order_counter}"
        Order.order_counter += 1
        self.__customer = customer
        self.__items = items  # list of {product, quantity}
        self.__date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__status = "Pending"
        self.__total = self.__calculate_total()

    def __calculate_total(self):
        total = 0
        for item in self.__items:
            total += item["product"].get_price() * item["quantity"]
        return round(total, 2)

    def get_order_id(self):
        return self.__order_id

    def get_total(self):
        return self.__total

    def get_status(self):
        return self.__status

    def update_status(self, status):
        valid = ["Pending", "Confirmed", "Shipped", "Delivered", "Cancelled"]
        if status in valid:
            self.__status = status
        else:
            print(f"  Invalid status! Choose from: {valid}")

    def get_summary(self):
        lines = [
            f"\n  {'='*50}",
            f"  Order ID   : {self.__order_id}",
            f"  Customer   : {self.__customer.get_name()}",
            f"  Date       : {self.__date}",
            f"  Status     : {self.__status}",
            f"  {'-'*50}",
            f"  {'Item':<30} {'Qty':>5} {'Price':>10}"
        ]
        for item in self.__items:
            p = item["product"]
            lines.append(f"  {p.get_name():<30} {item['quantity']:>5} Rs.{p.get_price():>8.2f}")
        lines.append(f"  {'-'*50}")
        lines.append(f"  {'TOTAL':>36} Rs.{self.__total:>8.2f}")
        lines.append(f"  {'='*50}")
        return "\n".join(lines)