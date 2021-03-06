# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
def start_module():
    table = data_manager.get_table_from_file("selling/sellings.csv")
    handle_menu()
    back_to_main = 0
    while not back_to_main:
        inputs = ui.get_inputs(["Enter a number:"], "")
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
            ui.print_result(get_lowest_price_item_id(table), "The id of the lowest priced items : ")
        elif option == "6":
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif option == "0":
            back_to_main = 1
        else:
            print_error_message("There is no such option")


# list_labels = ["id", "title", "price", "month", "day", "year"]


def handle_menu():
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Get lowest prite item id",
               "Get items sold between"]

    ui.print_menu("Menu", options, "Back to main menu")


# print the default table of records from the file
#
# @table: list of lists


# def show_table(table):


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists


def add(table):
    table = common.add(table, list_labels, "selling/sellingss.csv")
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string


# def remove(table, id_):
#     return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
# def update(table, id_):
#
#     # your code
#
#     return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    price = []
    i_d = []
    for i in table:
        price.append(i[2])
        i_d.append(i[0])
    mini = None
    for i in price:
        if mini is None:
            mini = i
        elif mini > i:
            mini = i
    final = []
    i = 0
    for e in price:
        if mini == e:
            final.append(i_d[i])
        i += 1
    return final


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code
    pass
