# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
def handle_menu():
    options = ["Show Table",
               "Add",
               "Remove",
               "Update",
               "Oldest person",
               "Closest to the average"]

    ui.print_menu("HR", options, "Return to Main menu")


def start_module():
    table = data_manager.get_table_from_file("hr/persons.csv")
    back_to_main = 0
    while not back_to_main:
        handle_menu()
        inputs = ui.get_inputs(["Please enter a number: "], "")
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
            get_oldest_person(table)
        elif option == "6":
            get_persons_closest_to_average(table)
        elif option == "0":
            back_to_main = 1
        else:
            print_error_message("There is no such option")
            break


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

    # your code

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    name = []
    year = []
    mini = None
    for row in table:
        if mini is None:
            mini = int(row[2])
        name.append(row[1])
        year.append(int(row[2]))
        if mini > int(row[2]):
            mini = int(row[2])
    final = []
    i = 0
    for element in year:
        if element == mini:
            final.append(name[i])
        i += 1
    ui.print_result(final, "The oldest people is/are : ")


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    name = []
    year = []
    total = 0
    nr_people = 0
    for row in table:
        nr_people += 1
        total = total + int(row[2])
        name.append(row[1])
        year.append(int(row[2]))
    average = total/nr_people
    final = []
    difference = []
    for element in year:
        if element < average:
            difference.append(average - element)
        elif element > average:
            difference.append(element - average)
        else:
            difference.append(0)
    mini = None
    for element in difference:
        if mini is None:
            mini = element
        if mini > element:
            mini = element
    i = 0
    for elem in difference:
        if mini == elem:
            final.append(name[i])
        i += 1
    ui.print_result(final, "The people closest to the average age is/are: ")
