# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Reece Wonio, 6/7/2022, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    def __init__(self, product_name: str, product_price: float):
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))

# Properties --
# Product Name

    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value: str):
        if str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Product Must be in Letters")

# Product Price --

    @property
    def product_price(self):
        return float(self.__product_price)  # cast to float

    @product_price.setter
    def product_price(self, value: float):
        if str(value).isnumeric():
             self.__product_price = float(value)  # cast to float

        else:
            raise Exception("Prices Must Be Numbers")

# Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + "," + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    @staticmethod # Saving Data to the File
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
                file.close()
                success_status = True
        except Exception as e:
            print("There was an Error")
            print(e, e.__doc__, type(e), sep='\n')
            return success_status

    @staticmethod # Reading Data from the File
    def read_data_from_file(file_name: str):
        lst_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], float(data[1]))
                lst_of_product_rows.append(row)
                file.close()
        except Exception as e:
            print("There was an Error!")
            print(e, e.__doc__, type(e), sep='\n')
            return lst_of_product_rows
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user """

    print('''
     Menu of Options
     1) Show current data
     2) Add a new item.
     3) Save Data to File
     4) Exit Program
     ''')
    print()

    @staticmethod
    def input_menu_choice():
        choice = str(input("Please Choose Option 1, 2, 3, or 4: "))
        print()
        return choice

    @staticmethod
    def print_current_list_of_products(list_of_rows: list):
        print("******** Your Current List of Products Is:********")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()

    @staticmethod
    def input_product_data():
        try:
            name = str(input("Enter a Product Name: ").strip())
            price = float(input("Enter The Product's Price: ").strip())
            print()
            p = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)

        return p

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
    while True:
        IO.print_menu_items()
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            IO.print_current_list_of_products(lstOfProductObjects)
            continue
        elif strChoice.strip() == '2':
            lstOfProductObjects.append(IO.input_product_data())
            continue
        elif strChoice.strip() == '3':
         FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
         continue
        elif strChoice.strip() == '4':
            break
except Exception as e:
    print("There was an Error! Check File Permissions")
    print(e, e.__doc__, type(e), sep='\n')

 # ---- END ---- #