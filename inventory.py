# ========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (
            f"{self.country},{self.code},{self.product},"
            f"{int(self.cost)},{int(self.quantity)}"
        )


# =============Shoe list===========
"""
The list will be used to store a list of objects of shoes.
"""
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    # ======= Explanation ========
    """
    The method first clears the list (to prevent the user
    from re-reading the same data). It then reads the information
    from the text file, separates them into smaller sections:
        - country
        - code
        - product
        - price
        - quantity
    and adds them to the shoe_list. First the data needs to be
    converted into readable string, hence the __str__() method.
    """
    # ============================

    shoe_list.clear()
    try:
        with open("inventory.txt", "r", encoding="utf-8") as read_data:
            lines = read_data.readlines()[1:]
            for line in lines:
                data = line.strip().split(",")
                country = data[0]
                code = data[1]
                product = data[2]
                cost = data[3]
                quantity = data[4]

                shoes = Shoe(country, code, product, int(cost), int(quantity))
                shoe_list.append(f"{shoes.country},{shoes.code},{shoes.product},{shoes.cost},{shoes.quantity}")

    except FileNotFoundError:
        print("It appears that the file does not exist")


def capture_shoes(in_country, in_code, in_product, in_cost, in_quantity):
    # ======= Explanation ========
    """
    The method takes the user's input from the menu,
    inputs them to the shoe object, then appends the
    shoes into the list, where it is converted into readable
    string. It also appends the input to the text file.
    """
    # ============================

    shoes = Shoe(in_country, in_code, in_product, in_cost, in_quantity)
    print("\nCapturing user input.......")
    print("Storing data.....")
    with open("inventory.txt", "a", encoding="utf-8") as update_file:
        update_file.writelines(
            f"\n{in_country},{in_code},{in_product},{in_cost},{in_quantity}"
        )
    shoe_list.append(f"{shoes.country},{shoes.code},{shoes.product},{shoes.cost},{shoes.quantity}")
    print("Data successfully captured!\n")
    read_shoes_data()


def view_all():
    # ======= Explanation ========
    """
    The method takes the list, separates the lines into smaller
    sections, formats and prints the each line. To make it
    readable for the user.
    """
    # ============================
    try:
        print(
            f"{'Country': ^15} {'Code': ^11} {'Product': ^16} "
            f"{'Cost': ^18} {'Quantity': ^4}"
        )
        for count, lines in enumerate(shoe_list, start=1):
            data = lines.strip().split(",")
            country = data[0]
            code = data[1]
            product = data[2]
            cost = data[3]
            quantity = data[4]

            print(
                f"{count: <2} {country: <15} {code: <12}"
                f"{product: <20} {cost: <15} {quantity: <4}"
            )
        print("")
    except Exception:
        print("The list is empty, please populate list.")


def re_stock():
    try:
        # ===== Explanation =====
        """
        The purpose of this method is to re-stock shoes that is
        almost out-of-stock. A new list will be created to convert and
        store the quantity. Using the new list, the minimum quantity can
        be found, converted to a string. We use that same string to compare
        the quantity to find the quantity that is exactly the same, print
        the line, ask the user if they would like to update the quantity.
        If the user says yes, update the quantity in the text file, and
        the shoe object.
        """
        # =======================

        # ====== Sources ========
        # Struggled to convert the quantity to an integer (lines: 135 - 142)
        # Reference: https://stackoverflow.com/questions/26051749/how-can-i-convert-the-index-of-a-string-to-an-integer-in-python
        # Reference: https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
        # Reference: https://stackoverflow.com/questions/28618342/find-min-and-max-from-text-file-python

        # Stuggled to update the file (lines: 171 -177)
        # Reference: https://stackoverflow.com/questions/45187646/python-how-to-write-to-specific-line-in-existing-txt-file
        # Reference: https://www.geeksforgeeks.org/python-program-to-replace-specific-line-in-file/
        # =======================

        new_shoes = []
        new_shoes.clear()

        for lines in shoe_list:
            data = lines.strip().split(",")
            quantity = data[4]

            for i in range(4, len(data)):
                data[i] = int(data[i])
            new_shoes.append((data[i]))

        min_quant = min(new_shoes)
        str_min_quant = str(min_quant)

        for count, line in enumerate(shoe_list, start=1):
            data = line.strip().split(",")
            country = data[0]
            code = data[1]
            product = data[2]
            cost = data[3]
            quantity = data[4]

            if str_min_quant == quantity:
                print(
                    f"{count} {country: <15} {code: <10}"
                    f"{product: <20} {cost: <15} {quantity: <4}\n"
                )

                restock = input(
                    f"Would you like to re-stock {product} (yes/no): "
                ).lower()

                if restock == "yes":
                    while True:
                        try:
                            update_inv = int(input("How many shoes need to be shipped: "))
                            break
                        except ValueError:
                            print("Incorrect input, only enter integers (numbers).")

                    quantity = str(update_inv)

                    with open("inventory.txt", "r", encoding="utf-8") as update_line:
                        lines = update_line.readlines()

                    lines[count] = f"{country},{code},{product},{cost},{quantity}\n"

                    with open("inventory.txt", "w", encoding="utf-8") as update_line:
                        update_line.writelines(lines)

                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.pop((count - 1))
                    shoe_list.insert((count - 1), shoe.__str__())

                    print(
                        f"{count} {country: <15} {code: <10}"
                        f"{product: <20} {cost: <15} {quantity: <4}"
                    )
                    print("")

                elif re_stock == "no":
                    print(
                        f"{count} {country: <15} {code: <10}"
                        f"{product: <20} {cost: <15} {quantity: <4}\n"
                    )

    except FileNotFoundError:
        print("The files does not exist, check if the file name is correct.")

    except Exception:
        print("Opps, someting went wrong. Please try again later.")


def seach_shoe(in_code):
    # ======= Explanation ========
    """
    The method takes user input and searches
    the list, the code section, and prints
    the code (and the rest of the details) user
    is looking for.
    """
    # ============================
    for lines in shoe_list:
        data = lines.strip().split(",")
        country = data[0]
        code = data[1]
        product = data[2]
        cost = data[3]
        quantity = data[4]

        if in_code in code:
            print(
                f"{country: <15} {code: <10}"
                f"{product: <20} {cost: <15} {quantity: <4}\n"
            )


def value_per_item():
    # ======= Explanation ========
    """
    This function will calculate the total value for each item.
    The value (quantity * cost) for each item is kept in a
    separate list (value), then both the shoe_list and value
    lists are combined and store in another list called new_shoe_list.
    Then the data is separated, then printed to make it easier for the user
    to read
    """
    # ============================

    # ========= Sources ==========
    # Struggles multipling the values in cost and quantity (lines: 287 - 288)
    # Reference: https://blog.enterprisedna.co/how-to-multiply-lists-in-python/
    # Reference: https://www.adamsmith.haus/python/answers/how-to-multiply-two-lists-in-python

    # Struggled to combined values and shoe_list to make them one list without
    # add it to the end of the new list. (lines: 290 - 291)
    # Reference: https://stackoverflow.com/questions/52374104/typeerror-unsupported-format-string-passed-to-list-format

    # ============================

    try:
        value = []
        cost_list = []
        quant_list = []
        new_shoe_list = []

        value.clear()
        cost_list.clear()
        quant_list.clear()
        new_shoe_list.clear()

        for lines in shoe_list:
            data = lines.strip().split(",")
            cost = data[3]

            for i in range(3, len(cost)):
                data[i] = int(data[i])
                cost_list.append(data[i])

            for i in range(4, len(data)):
                data[i] = int(data[i])
                quant_list.append(data[i])

        for i, j in zip(cost_list, quant_list):
            value.append(str(i * j))

        for shoes, val in zip(shoe_list, value):
            new_shoe_list.append((f"{shoes},{val}"))

        print(
            f"{'Country': ^15} {'Code': ^11} {'Product': ^16} "
            f"{'Cost': ^18} {'Quantity': ^4} {'Value': ^11}"
        )

        for count, lines in enumerate(new_shoe_list):
            data = lines.strip().split(",")
            country = data[0]
            code = data[1]
            product = data[2]
            cost = data[3]
            quantity = data[4]
            val = data[5]

            print(
                f"{(count+1): <2} {country: <15} {code: <12}"
                f"{product: <20} {cost: <12} {quantity: <10} {val: <7}"
            )

        print("")

    except IndexError:
        print("Index our of range!")

    except Exception:
        print("Something went wrong.")


def highest_qty():
    # ======== Explanation ========
    """
    The method finds the highest quantity in the shoe list
    then prints that it's on sale.
    The method creates a new list to store the int quantity, finds the
    max of the quantity, converts the ans to a string. Then the method
    then takes the string max value and if the value equals to a value
    in quantity print the shoe details and state that it is for sale.
    """
    # =============================

    new_shoes = []
    new_shoes.clear()

    for lines in shoe_list:
        data = lines.strip().split(",")
        quantity = data[4]

        for i in range(4, len(data)):
            data[i] = int(data[i])
            quantity = data[i]
            new_shoes.append((quantity))
    max_quant = max(new_shoes)

    str_max_quant = str(max_quant)

    for count, lines in enumerate(shoe_list, start=1):
        data = lines.strip().split(",")
        country = data[0]
        code = data[1]
        product = data[2]
        cost = data[3]
        quantity = data[4]

        if str_max_quant == quantity:
            print(
                f"\n{count} {country: <15} {code: <10}"
                f"{product: <20} {cost: <15} {quantity: <4}\n"
            )
            print(f"The {product} is on sale in {country}!\n")


# ==========Main Menu=============
while True:
    menu = input(
        """Select one of the following options:
r - Read shoe data
c - Capture shoe data
va - View all shoe data
rs - Re-stock shoes
s - Search for shoes
vi - Value per item
h - highest quantity
e - exit
: """
    ).lower()

    if menu == "r":
        read_shoes_data()
        print("\nShoe data successfully read!\n")

    elif menu == "c":
        country = input("Enter the name the region (country): ")
        code = input(
            "Enter the Nike product code (must start with SKU, "
            "the rest are numbers, max length = 8): "
        )

        if len(code) != 8:
            while len(code) != 8:
                code = input(
                    "The character length is either smaller or greater than 8\n"
                    "Please enter an 8 length code that starts with SKU: "
                )

                if len(code) == 8:
                    if "SKU" not in code:
                        while "SKU" not in code:
                            code = input(
                                "The code does not contain SKU.\n"
                                "Please enter an 8 length code that starts with SKU: "
                            )

        else:
            if "SKU" not in code:
                while "SKU" not in code:
                    code = input(
                        "The code does not contain SKU.\n"
                        "Please enter an 8 length code that starts with SKU: "
                    )

        product = input("Enter the name of the Nike product: ")

        while True:
            try:
                cost = int(input("Enter the cost of the Nike product (no decimals): "))
                break
            except ValueError:
                print("Sorry, only integer values will be captured")

        while True:
            try:
                quantity = int(input("Enter the quantity in stock: "))
                break
            except ValueError:
                print("Sorry, only integer values will be captured")

        capture_shoes(country, code, product, cost, quantity)

    elif menu == "va":
        view_all()

    elif menu == "rs":
        pass
        re_stock()

    elif menu == "s":
        in_code = input(
            "Enter the code for the shoes you wish to look for (SKU + 5 numbers): "
        )
        seach_shoe(in_code)

    elif menu == "vi":
        value_per_item()

    elif menu == "h":
        highest_qty()

    elif menu == "e":
        print("\nEnjoy your day!")
        exit()

    else:
        print(
            "Opps, invalid input! Please enter any of the options stated in the menu.\n"
        )