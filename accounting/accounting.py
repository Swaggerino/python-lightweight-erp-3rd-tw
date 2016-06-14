# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
# import main
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()
# main = SourceFileLoader("python-lightweight-erp-3rd-tw", current_file_path + "/../main.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Tool manager",
               "Accounting manager",
               "Selling manager",
               "Customer Relationship Management (CRM)"]

    ui.print_menu("Main menu", options, "Exit program")


def start_module():
    inputs = ui.get_inputs("Please: ", "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add_table()
    elif option == "3":
        remove(table, id_)
    elif option == "4":
        update(table, id_)
    elif option == "5":
        which_year_max(table)
    elif option == "6":
        avg_amount(table, year)
    # elif option == "0":
    #     # main.main()
    else:
        raise KeyError("There is no such option.")
    # table = data_manager.get_table_from_file("items.csv")
    # you code

    pass

start_module()

# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    ui.print_table(table, )

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    common.add_table()
    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
