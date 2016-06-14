# implement commonly used functions here
import data_manager
import random
import ui

# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):
    while True:
        generated = ''

        letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "!@#$%^&*()?"
        generated += letters[random.randrange(0, len(letters))]
        generated += letters[random.randrange(0, len(letters))].upper()
        generated += numbers[random.randrange(0, len(numbers))]
        generated += numbers[random.randrange(0, len(numbers))]
        generated += letters[random.randrange(0, len(letters))].upper()
        generated += letters[random.randrange(0, len(letters))]
        generated += symbols[random.randrange(0, len(symbols))]
        generated += symbols[random.randrange(0, len(symbols))]
        if generated not in table:
            break
    return generated


def add(table, list_labels, file_name):
    inputs = ui.get_inputs(list_labels, "")
    table.append(inputs)
    data_manager.write_table_to_file(table, file_name)
    return table
