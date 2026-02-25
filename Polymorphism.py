def display_info(obj):
    print(obj.get_details() if hasattr(obj, "get_details") else obj.get_profile())


# MAIN FUNCTION

def main():

    print("\n===== 4 PILLARS OF OOP DEMO =====")

    # Inheritance
    p1 = Clothing("P001", "T-Shirt", 1200, "M")

    # Encapsulation
    print("\nEncapsulation Example:")
    print(p1.get_details())
    p1.set_price(1500)
    print("Updated Price:", p1.get_details())

    # Abstraction + Inheritance
    cust = Customer("C001", "Ayesha")
    admin = Admin("A001", "Usman")

    # Polymorphism
    print("\nPolymorphism Example:")
    display_info(p1)
    display_info(cust)
    display_info(admin)


if __name__ == "__main__":
    main()