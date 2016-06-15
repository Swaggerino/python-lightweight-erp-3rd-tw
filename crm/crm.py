# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
file_name = "crm/customers.csv"
menu_status = 0
# load table from file
table = data_manager.get_table_from_file(file_name)
# list of menu options
menu_options = ["Show customers",
                "Add customer to the table",
                "Remove customer from the table",
                "Update an item in the table",
                "Get the id of customer with the longest name in the table",
                "Get the name of the customer with the most subscription"]
list_labels = ["id", "name", "email", "subscribed"]
update_labels = ["name", "email", "subscribed"]
id_list = ["id"]

# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#


def start_module():
    global menu_status
    ui.print_menu("Customer Relationship Management (CRM)", menu_options, "Exit program")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    menu_status = 0
    while True:
        if option == "1":
            show_table(table)
            break
        elif option == "2":
            common.add(table, list_labels, file_name)
            break
        elif option == "3":
            remove(table, id_)
            break
        elif option == "4":
            id_input = ui.get_inputs(id_list, "")
            updated_table = []
            updated_table = common.update(table, update_labels, id_input[0])
            data_manager.write_table_to_file(file_name, updated_table)
            break
        elif option == "5":
            get_longest_name_id(table)
            ui.print_result(get_longest_name_id(table), "The People with the longest name is/are: ")
            break
        elif option == "6":
            get_subscribed_emails(table)
            break
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        start_module()


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

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

    return table


# special functions:
# ------------------

# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    name = []
    id_ = []
    for row in table:
        id_.append(row[0])
        name.append(row[1])
    longest = None
    for element in name:
        if longest is None:
            longest = len(element)
        if len(element) > longest:
            longest = len(element)
    final = []
    i = 0
    for element in name:
        if longest == len(element):
            final.append(id_[i])
        i += 1
    # ui.print_result(final, " text ")
    return final


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
