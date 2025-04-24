#!/usr/bin/env python3

"""Showcase that type hints do not prevent wrong usage of a function parameter.
It is just a hint for the developer and not a constraint for the interpreter.
Thus if one want to be sure, asserts or any other checks are needed."""


def blub(a: str):
    assert isinstance(a, str), "'a' is not a 'str'"
    print(a)


if __name__ == "__main__":
    blub("hello")  # Intended use
    blub(123)  # Wrong usage, but if there would be no assert in the function, no error would be raised.
