# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Reece Wonio,5/15/22,Added Dictionary):
# RRoot,1.1.2030,Created started script
# Reece Wonio, 5/15/22, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open("ToDoList.txt", 'a')
dicRow = {'Task': 'Mow', 'Priority': 'High'}
objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
lstTable = [dicRow]
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open("ToDoList.txt", "r")
        for row in objFile:
            lstTable = row.split(",")
            dicRow = {"Task": lstTable[0], "Priority": lstTable[1].strip()}
            print(dicRow["Task"] + '|' + dicRow["Priority"])

        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strData = input("Task: ")
        strPri = input("Priority: ")
        lstTable.append({"Task": strData, "Priority": strPri})
        continue
    # Step 5 - Remove a item from the list/Table
    elif (strChoice.strip() == '3'):
        strData = input("Task to Remove: ")
        for row in lstTable:
            if row["Task"] == strData:
                lstTable.remove(row)
                print("Task Removed")
                print(lstTable)
            else:
                print("Task Not Found")
                print(lstTable)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "a")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ',' + str(row["Priority"]) + '\n')
            objFile.close()
            print("Now in File!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("You Have Exited the Program")
        break  # and Exit the program
    else:
        print("Please only enter 1, 2, 3, 4, or 5")

