

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table

# title_list = ('id', 'month', 'day', 'year', 'type', 'amount')
# table = (("kH14Ju#&", 1, 21, 2016, "in", 31),
#          ("kH38Jm#&", 10, 23, 2016, "out", 40))


def print_table(table, title_list):

    all_length = 0
    col_lengths = []
    to_print = ""

    for elem in title_list:
        all_length += len(elem) + 2
        col_lengths.append(len(elem) + 2)
    for rows in table:
        i = 0
        row_length = 0
        for elem in rows:
            row_length += len(str(elem)) + 2
            if len(str(elem)) + 2 > col_lengths[i]:
                col_lengths[i] = len(str(elem)) + 2
            i += 1
        if row_length > all_length:
            all_length = row_length

    if sum(col_lengths) + 2 * len(title_list) > all_length:
        all_length = sum(col_lengths)  + 2 * len(title_list)

    to_print += "/{0}\\\n|".format((all_length + (len(title_list) - 1)) * "-")  # /----\
    i = 0
    for elem in title_list:  # prints head
        diff = col_lengths[i] - len(elem)
        to_print += " {0} |".format(elem + diff * " ")
        i += 1
    for lst in table:
        to_print += "\n|"
        for elem in col_lengths:  # ---|---|---|
            to_print += "{0}|".format((elem + 2) * "-")
        to_print += "\n|"
        for elem in lst:  # table content | table content |
            to_print += " {0} |".format(elem)
    to_print += "\n\\{0}/".format((all_length + (len(title_list) - 1)) * "-")  # \----/
    print(to_print)

# print_table(table, title_list)
# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    # your code

    pass


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):

    # your code

    pass


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []

    # your code

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    # your code

    pass
