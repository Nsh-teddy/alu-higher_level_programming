#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
