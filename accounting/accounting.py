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
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#

def handle_menu():
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Which year max",
               "Avg amount"]

    ui.print_menu("Menu", options, "Back to main menu")

table = data_manager.get_table_from_file("accounting/items.csv")
list_labels = ["nr1", "nr2", "nr3", "fd", "ffd"]


def start_module():
    handle_menu()
    back_to_main = 0
    while not back_to_main:
        inputs = ui.get_inputs(["Please:"], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove(table, id_)
        elif option == "4":
            update(table, id_)
        elif option == "5":
            which_year_max(table)
        elif option == "6":
            avg_amount(table, year)
        elif option == "0":
            back_to_main = 1
        else:
            print_error_message("There is no such option")

# handle_menu()
# start_module()

# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    ui.print_table(table, list_label)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    table = common.add(table, list_labels, "accounting/items.csv")
    # print(table)
    # # your code

    return table
def add(table, list_labels, file_name):
    id_ = [generate_random(table)]
    inputs = (id_ + ui.get_inputs(list_labels, ""))
    table.append(inputs)
    data_manager.write_table_to_file(file_name, table)
    return table

# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    id_index = table.index(id_)

    # table.remove(row[range(0, len(title_list))])
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
