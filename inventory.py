# ---------------------- Shoe Class ----------------------

# define Shoe class

class Shoes:

    # create class attributes

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # define class methods

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_product(self):
        return self.product

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"+"\n"

# ---------------------- Helper functions ----------------------

# open the file inventory.txt and read the data

def read_shoes_data():
    read_file = None
    try:
        read_file = open("inventory.txt", "r")
        inventory_file = read_file.readlines()[1:]

        for lines in inventory_file:
            strip_lines = lines.strip("\n")
            country,code,product,cost,quantity = strip_lines.split(",")
            shoe = Shoes(country,code,product,float(cost),int(quantity))
            list_shoe_obj.append(shoe)

    except FileNotFoundError as error:
        print("\nfile does not exist!\n")
        print(error)

    finally:
        if read_file is not None:
            read_file.close()

def write_shoe_data(): 
    output_file = None
    try:
        output_file = open("inventory.txt", "w")

        if len(list_shoe_obj) < 1:
            print("No items in stock")
        else: 
            output_file.write("Country,Code,Product,Cost,Quantity \n")
            for shoe_item in list_shoe_obj: 
                output_file.write(shoe_item.__str__())

    except FileNotFoundError as error:
        print("\nfile does not exist!\n")
        print(error)

    finally:
        if output_file is not None:
            output_file.close()

# allow a user to capture data about a shoe and use this data to create a shoe object 

def capture_shoes():
    print("Capture shoe details to file\n")
    country= input("Enter the shoe country: ") 
    code= input("Enter the shoe code: ")
    product = input("Enter the shoe product: ")
    cost= input("Enter the shoe cost: ")
    quantity = input("Enter the shoe quantity: ") 

    new_shoe = Shoes(country, code, product, cost, quantity)
    list_shoe_obj.append(new_shoe)

    # add the new shoe data to the file 
    write_shoe_data()
    print("Shoe added!")

# function will iterate over all the shoes list and print the details of the shoes

def view_all():
    if len(list_shoe_obj) < 1:
        print("No items in stock")
    else: 
        for shoe_item in list_shoe_obj: 
            print(shoe_item.__str__())

# find the shoe object with the lowest quantity, restock shoes with list

def re_stock(): 
    lowest_quantity = 0
    index = 0
    item = {}
    for line in list_shoe_obj:
        if index == 0 : 
            lowest_quantity = line.get_quantity()
            
        else : 
            if line.get_quantity() < lowest_quantity:
                lowest_quantity = line.get_quantity()
                item = line

        index = index + 1
    print(f"Product: {item.product} has a quantity of {item.quantity}")

    # Check if user wanted to restock low quantity item 
    reStock_item = input("Would you like to re stock the item? Y/N: ").upper()
    if reStock_item == "Y":
        try:
            update_quantity = int(input("Enter updated quantity amount: "))
            item.quantity = update_quantity
            write_shoe_data()
            print("Stock updated !")

        except ValueError:
            print("\nInvalid input, enter a number.\n")

# This function will search for a shoe from the list and return this object and be printed

def search_shoe():
    if len(list_shoe_obj) < 1:
        print("No items in stock to search")
    else: 
        shoe_code = input("Enter shoe code: ")

        for shoe in list_shoe_obj: 
            if shoe_code == shoe.code: 
                print(shoe.__str__())
                break

# function will calculate the total value for each item

def value_per_item():
    for line in list_shoe_obj:
        value = ((line.get_cost()) * (line.get_quantity()))
        print(f'{line.product} Value: R{value}\n')

# the product with the highest quantity and print this shoe as being for sale

def highest_qty():
    highest_quantity = 0
    item = {}
    for line in list_shoe_obj:
        if line.get_quantity() > highest_quantity:
            highest_quantity = line.get_quantity()
            item = line
    print(item.product, highest_quantity)

# ---------------------- Main Function ----------------------

while True:
    list_shoe_obj = []
    read_shoes_data()

    try:
        menu = int(input('''\n
            Inventory System! 
            Please select from the menu below:

            1. Capture Shoes
            2. View All
            3. Restock
            4. Search
            5. View Item Values
            6. View Sale Items
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            re_stock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_qty()

        elif menu > 6:
            print("\nInvalid option. Please try again by choosing from the menu below.\n")

    except ValueError:
        print("\nInvalid input, Please try again by entering a number.\n")
