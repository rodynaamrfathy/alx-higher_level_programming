#!/usr/bin/python3
"""a class MyList that inherits from list
prints the list, but sorted (ascending sort)"""


class MyList(list):
    """Class MyList inherits from list"""

    def print_sorted(self):
        """Prints the list, in ascending order"""

        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
