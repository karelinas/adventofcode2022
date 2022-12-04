"""
Advent of Code 2022 day 01 solution.

To run with puzzle input:

    python3 day01.py < input/day01.txt

To run doctests:

    python3 -m doctest day01.py
"""

from sys import stdin
from typing import List, TextIO

ElfInventory = List[int]


def main():
    """Prints solutions for Advent of Code 2022 day 1"""
    inventories: List[ElfInventory] = parse_inventories(stdin)
    print(most_calories(inventories))
    print(sum_of_top_three_calories(inventories))


def most_calories(inventories: List[ElfInventory]) -> int:
    """Returns the sum of calories in the inventory with most calories

    >>> example_input = [
    ...     [1000, 2000, 3000],
    ...     [4000],
    ...     [5000, 6000],
    ...     [7000, 8000, 9000],
    ...     [10000]
    ... ]
    >>> most_calories(example_input)
    24000
    """
    return max(sum(cal for cal in inventory) for inventory in inventories)


def sum_of_top_three_calories(inventories: List[ElfInventory]) -> int:
    """Returns the total of calories in the top three inventories

    >>> example_input = [
    ...     [1000, 2000, 3000],
    ...     [4000],
    ...     [5000, 6000],
    ...     [7000, 8000, 9000],
    ...     [10000]
    ... ]
    >>> sum_of_top_three_calories(example_input)
    45000
    """
    sums: List[int] = [sum(cal for cal in inventory) for inventory in inventories]
    return sum(sorted(sums, reverse=True)[:3])


def parse_inventories(file_in: TextIO) -> List[ElfInventory]:
    r"""Parse list of calories to a list of inventories

    >>> from io import StringIO
    >>> example_input = (
    ...     "1000\n2000\n3000\n\n"
    ...     "4000\n\n5000\n6000\n\n"
    ...     "7000\n8000\n9000\n\n"
    ...     "10000\n"
    ... )
    >>> with StringIO(example_input) as f:
    ...     parse_inventories(f) == [
    ...         [1000, 2000, 3000],
    ...         [4000],
    ...         [5000, 6000],
    ...         [7000, 8000, 9000],
    ...         [10000]
    ...     ]
    True
    """

    return [
        [int(cal) for cal in inventory.strip().split("\n")]
        for inventory in file_in.read().split("\n\n")
    ]


if __name__ == "__main__":
    main()
