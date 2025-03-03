#!/usr/bin/env python3

"""Small script to verify if a 'default' value is needed when using 'store_true' action in argparse.
Answer --> No.
"""

import argparse


def _parse_args():
    parser = argparse.ArgumentParser(
        description="There is no default value needed when using 'store_true'."
    )

    parser.add_argument(
        "-s",
        "--store_value",
        action="store_true",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    print(f"args.store_value is {args.store_value}")
