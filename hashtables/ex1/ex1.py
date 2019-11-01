#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # create list to hold the index of weights

    # loop through the weights
        # check if weight - item is in ht
            # if it is add its position and the position of weight - item to the tuple
            # otherwise, add item and index to the tuple as key/value pair

    # return the sorted tuple

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
