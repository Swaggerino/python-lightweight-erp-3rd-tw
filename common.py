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
    generate = True
    while generate:
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
        ids = []
        for lists in table:
            ids.append(lists[0])
        if generated not in ids:
            generate = False
    return generated


def add(table, list_labels, file_name):
    id_ = [generate_random(table)]
    inputs = (id_ + ui.get_inputs(list_labels, ""))
    table.append(inputs)
    data_manager.write_table_to_file(file_name, table)
    return table


def update(table, list_labels, id_):
    new_data = []
    updated_id = 0
    inputs = ui.get_inputs(list_labels, "")
    table_len = len(table)
    inputs.insert(0, id_)
    for id in range(table_len):
        if table[id][0] == inputs[0]:
            table[id] = inputs
            break
    print(table[id])
    #data_manager.write_table_to_file(file_name, table)
    return table


def remove(table, id_):
    def remove(table, id_):
        for i in range(len(table)):
            if table[i][0] == id_:
                del table[i]

        return table
