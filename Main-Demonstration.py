def main():
    print("\n" + "="*65)
    print("   STYLE ARENA - Online Shopping Management System")
    print("   Demonstrating All 4 Pillars of OOP")
    print("="*65)

    system = ShoppingManagementSystem("Style Arena")

    # ---- PILLAR 1: ABSTRACTION ----
    print("\n" + "-"*65)
    print("  PILLAR 1: ABSTRACTION")
    print("  AbstractProduct & AbstractUser are abstract blueprints.")
    print("  They cannot be instantiated directly - only subclasses can.")
    print("-"*65)

    # ---- PILLAR 3: INHERITANCE - Create Products ----
    print("\n" + "-"*65)
    print("  PILLAR 3: INHERITANCE")
    print("  MaleClothing, FemaleClothing, UnisexClothing inherit from Product")
    print("  Customer & Admin inherit from User")
    print("-"*65)

    # Male Products
    m1 = MaleClothing("M001", "Classic Oxford Shirt",  2500, 30, "M",  "White",     "Shirt")
    m2 = MaleClothing("M002", "Denim Slim Fit Jeans",  3200, 20, "L",  "Blue",      "Trouser")
    m3 = MaleClothing("M003", "Embroidered Kurta",     1800, 25, "XL", "Navy Blue", "Kurta")
    m4 = MaleClothing("M004", "Casual Hoodie",         2200, 15, "M",  "Grey",      "Jacket")

    # Female Products
    f1 = FemaleClothing("F001", "Floral Printed Kurti",   1500,  40, "S", "Pink",  "Kurti",    "Casual")
    f2 = FemaleClothing("F002", "Bridal Lehenga",        15000,   5, "M", "Red",   "Lehenga",  "Traditional")
    f3 = FemaleClothing("F003", "Office Formal Dress",    4500,  18, "M", "Black", "Dress",    "Formal")
    f4 = FemaleClothing("F004", "Cotton Shalwar Kameez",  2000,  35, "L", "Peach", "Shalwar",  "Traditional")

    # Unisex Products
    u1 = UnisexClothing("U001", "Graphic Tee",      900, 50, "M", "Black",      "T-Shirt")
    u2 = UnisexClothing("U002", "Fleece Tracksuit", 3500, 22, "L", "Dark Green", "Tracksuit")

    for product in [m1, m2, m3, m4, f1, f2, f3, f4, u1, u2]:
        system.add_product(product)

    # Register Users
    print()
    admin1 = Admin("A001", "Usman Khan",   "usman@stylearena.pk", "admin123", "0300-1111111", admin_level=2)
    cust1  = Customer("C001", "Ayesha Malik", "ayesha@gmail.com", "pass123",  "0321-2222222", "House 5, Gulberg, Lahore")
    cust2  = Customer("C002", "Bilal Ahmed",  "bilal@gmail.com",  "pass456",  "0333-3333333", "Block A, DHA, Karachi")

    system.register_admin(admin1)
    system.register_customer(cust1)
    system.register_customer(cust2)

    # ---- PILLAR 2: ENCAPSULATION ----
    print("\n" + "-"*65)
    print("  PILLAR 2: ENCAPSULATION")
    print("  Private attributes accessed only through getters/setters")
    print("-"*65)
    print(f"  Admin Profile  : {admin1.get_profile()}")
    print(f"  Customer       : {cust1.get_profile()}")
    print(f"  Password check (correct) : {'PASS' if cust1.verify_password('pass123') else 'FAIL'}")
    print(f"  Password check (wrong)   : {'PASS' if cust1.verify_password('hacked') else 'FAIL - access denied'}")

    # Show inventory
    system.show_inventory()

    # ---- PILLAR 4: POLYMORPHISM ----
    print("\n" + "-"*65)
    print("  PILLAR 4: POLYMORPHISM")
    print("  Same display_product_info() gives different output per type:")
    print("-"*65)
    for product in [m1, f1, u1]:
        display_product_info(product)
        print()

    # ---- CUSTOMER 1 SHOPPING ----
    print("-"*65)
    print("  SHOPPING SESSION: Ayesha Malik (Female Customer)")
    print("-"*65)
    cust1.add_to_cart(f1, 2)
    cust1.add_to_cart(f4, 1)
    cust1.add_to_cart(u1, 1)

    print("\n  Polymorphic Payment - Card:")
    card = CardPayment("4111111111111234", "Ayesha Malik")
    order1 = system.place_order(cust1, card)
    if order1:
        print(order1.get_summary())

    # ---- CUSTOMER 2 SHOPPING ----
    print("-"*65)
    print("  SHOPPING SESSION: Bilal Ahmed (Male Customer)")
    print("-"*65)
    cust2.add_to_cart(m1, 1)
    cust2.add_to_cart(m2, 2)
    cust2.add_to_cart(u2, 1)

    print("\n  Polymorphic Payment - EasyPaisa:")
    easypaisa = EasyPaisaPayment("0321-5555555")
    order2 = system.place_order(cust2, easypaisa)
    if order2:
        print(order2.get_summary())

    # ---- ADMIN: APPLY SALE ----
    print("-"*65)
    print("  ADMIN ACTION: Applying 15% discount on Female clothing")
    print("-"*65)
    system.apply_sale("Female", 15)

    print("\n  Updated Female Inventory After Sale:")
    system.show_inventory(gender_filter="Female")

    # ---- ORDER STATUS UPDATE ----
    if order1:
        order1.update_status("Shipped")
        print(f"\n  Order {order1.get_order_id()} status updated to: {order1.get_status()}")

    # ---- ALL ORDERS ----
    print("\n" + "-"*65)
    print("  ALL ORDERS IN SYSTEM")
    print("-"*65)
    system.show_all_orders()