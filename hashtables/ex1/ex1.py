#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # loop through the weights
    for i, item in enumerate(weights):
        # check if limit - item is in ht
        if hash_table_retrieve(ht, (limit - item)) is not None:
            # get the index of limit - item
            other_index = hash_table_retrieve(ht, (limit - item))

            # since the order matters, check the size of the index
            # of the weights and return in the correct ordr
            if i > other_index:
                return [i, other_index]
            else:
                return [other_index, i]
        # otherwise, add item and index to the tuple as key/value pair
        else:
            hash_table_insert(ht, item, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
