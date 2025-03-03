#!/usr/bin/env python3

"""Showcase why mutable default arguments are a bad idea."""


class SomeClass:
    def __init__(self, this_is_mutable=[]):
        self._my_list = this_is_mutable

    def __str__(self):
        return f"SomeClass: {self._my_list}"

    def __repr__(self):
        self.__str__()


if __name__ == "__main__":
    a = SomeClass([1, 2, 3])
    a.__init__()
    b = SomeClass()
    print(f"Instance a: {a}, initialized with '[1, 2, 3]'")
    print(f"Instance b: {b}, initialized with '[]'")
