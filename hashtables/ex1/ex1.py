#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # create list to hold the index of weights
    index = []

    # loop through the weights
    for i, item in enumerate(weights):
        # check if limit - item is in ht
        if hash_table_retrieve(ht, (limit - item)) is not None:
            # if it is add its position to the list
            index.append(i)
            # add the index of limit - item to the list as well
            index.append(hash_table_retrieve(ht, (limit - item)))
        # otherwise, add item and index to the tuple as key/value pair
        else:
            hash_table_insert(ht, item, i)

    # return the sorted tuple
    if len(index):
        return sorted(index, reverse=True)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
