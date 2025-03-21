#!/usr/bin/env python3

"""Showcase why mutable default arguments are a bad idea."""


class SomeClass:
    def __init__(self, this_is_mutable=[]):
        self.data = this_is_mutable

    def __str__(self):
        return f"SomeClass: {self.data}"

    def __repr__(self):
        self.__str__()


if __name__ == "__main__":
    print(
        " --- case 1: data gets changed outside of the class, but class member is affected:"
    )
    data = [1, 2, 3]
    a = SomeClass(this_is_mutable=data)

    data.append(13)
    print(f"Instance a: {a}, initialized with '[1, 2, 3]'")
    # Prints:
    # Instance a: SomeClass: [1, 2, 3, 13], initialized with '[1, 2, 3]'

    # -----------------------------------------------------------------------------------------

    print(
        "\n --- case 2: data is used for initializing two class instances, only one gets changed but both are affected:"
    )

    data = [23, 24, 13]
    a = SomeClass(this_is_mutable=data)
    b = SomeClass(this_is_mutable=data)

    a.data.append(999)

    print(f"Instance a: {a}")
    print(f"Instance b: {b}")
    # Prints:
    # Instance a: SomeClass: [23, 24, 13, 999]'
    # Instance b: SomeClass: [23, 24, 13, 999]'
