#!/usr/bin/env python3

"""Be aware that all mutable objects are passed by reference in Python.
Knowing this, the issues below can be avoided."""

import typing


class SomeClass:
    def __init__(self, data: typing.List[int]):
        self.data = data

    def __str__(self):
        return f"SomeClass: {self.data}"

    def __repr__(self):
        self.__str__()


if __name__ == "__main__":
    print(
        " --- case 1: data gets changed outside of the class, but class member is affected:"
    )
    data = [1, 2, 3]
    a = SomeClass(data=data)

    data.append(13)
    print(f"Instance a: {a}, initialized with '[1, 2, 3]'")
    # Prints:
    # Instance a: SomeClass: [1, 2, 3, 13], initialized with '[1, 2, 3]'

    # -----------------------------------------------------------------------------------------

    print(
        "\n --- case 2: data is used for initializing two class instances, only one gets changed but both are affected:"
    )

    data = [23, 24, 13]
    a = SomeClass(data=data)
    b = SomeClass(data=data)

    a.data.append(999)

    print(f"Instance a: {a}")
    print(f"Instance b: {b}")
    # Prints:
    # Instance a: SomeClass: [23, 24, 13, 999]'
    # Instance b: SomeClass: [23, 24, 13, 999]'
