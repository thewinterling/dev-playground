#!/usr/bin/env python3


def blub(a: str):
    assert isinstance(a, str), "'a' is not a 'str'"
    print(a)


if __name__ == "__main__":
    blub("hello")
    blub(123)
