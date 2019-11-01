#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # loop through the tickets
    for ticket in tickets:
        # add the tickets source/destination to the hashtable as pair
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # set a variable source to string None
    source = "NONE"
    # set a variable position to 0
    position = 0
    # loop while position is less than length
    while position < length:
        # get the destination for the source
        destination = hash_table_retrieve(hashtable, source)
        # set the value of source in route using the position
        route[position] = destination
        # set source to the destination
        source = destination
        # increment position
        position += 1

    return route
