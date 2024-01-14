#!/usr/bin/python3
"""
module containing code for:
    - class MyList
"""


class MyList(list):
    """the class representing the list.

    Extends:
        list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)

        Params:
            - self: this instance
        """

        sorted_list = self.copy()
        sorted_list.sort()
        print("{}".format(sorted_list))

        return sorted_list
