"""
Advent of Code 2022 day 04 solution.

To run with puzzle input:

    python3 day04.py < input/day04.txt

To run doctests:

    python3 -m doctest day04.py
"""

from sys import stdin
from typing import List, Set, TextIO, Tuple

SectionAssignment = Set[int]
SectionAssignmentPair = Tuple[SectionAssignment, SectionAssignment]
SectionAssignmentList = List[SectionAssignmentPair]


def main():
    """Prints solutions for Advent of Code 2022 day 4"""
    section_assignments: SectionAssignmentList = parse_section_assignments(stdin)
    print(count_fully_overlapping_assignments(section_assignments))
    print(count_overlapping_assignments(section_assignments))


def count_fully_overlapping_assignments(assignments: SectionAssignmentList) -> int:
    """Returns the count of section assignments where one of the pair fully overlaps the other

    >>> example_input = [
    ...     ({2, 3, 4}, {6, 7, 8}),
    ...     ({2, 3}, {4, 5}),
    ...     ({5, 6, 7}, {7, 8, 9}),
    ...     ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
    ...     ({6}, {4, 5, 6}),
    ...     ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8})
    ... ]
    >>> count_fully_overlapping_assignments(example_input)
    2
    """
    return sum(1 if one_fully_contains_the_other(a, b) else 0 for a, b in assignments)


def count_overlapping_assignments(assignments: SectionAssignmentList) -> int:
    """Returns the count of section assignments where one of the pair fully overlaps the other

    >>> example_input = [
    ...     ({2, 3, 4}, {6, 7, 8}),
    ...     ({2, 3}, {4, 5}),
    ...     ({5, 6, 7}, {7, 8, 9}),
    ...     ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
    ...     ({6}, {4, 5, 6}),
    ...     ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8})
    ... ]
    >>> count_overlapping_assignments(example_input)
    4
    """
    return sum(1 if one_overlaps_the_other(a, b) else 0 for a, b in assignments)


def one_fully_contains_the_other(a: SectionAssignment, b: SectionAssignment) -> bool:
    """Returns True if a is a subset or b or if b is a subset of a

    >>> one_fully_contains_the_other({2, 3, 4}, {6, 7, 8})
    False
    >>> one_fully_contains_the_other({2, 3}, {4, 5})
    False
    >>> one_fully_contains_the_other({5, 6, 7}, {7, 8, 9})
    False
    >>> one_fully_contains_the_other({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7})
    True
    >>> one_fully_contains_the_other({6}, {4, 5, 6})
    True
    >>> one_fully_contains_the_other({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8})
    False
    """
    return a.issubset(b) or b.issubset(a)


def one_overlaps_the_other(a: SectionAssignment, b: SectionAssignment) -> bool:
    """Returns True if a overlaps b

    >>> one_overlaps_the_other({2, 3, 4}, {6, 7, 8})
    False
    >>> one_overlaps_the_other({2, 3}, {4, 5})
    False
    >>> one_overlaps_the_other({5, 6, 7}, {7, 8, 9})
    True
    >>> one_overlaps_the_other({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7})
    True
    >>> one_overlaps_the_other({6}, {4, 5, 6})
    True
    >>> one_overlaps_the_other({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8})
    True
    """
    return not a.isdisjoint(b)


def parse_section_assignments(file_in: TextIO) -> SectionAssignmentList:
    r"""Parse pairs of section assignments from the input file

    >>> from io import StringIO
    >>> with StringIO("1-5,6-10\n") as f:
    ...     parse_section_assignments(f)
    [({1, 2, 3, 4, 5}, {6, 7, 8, 9, 10})]

    >>> example_input = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8\n"
    >>> with StringIO(example_input) as f:
    ...     parse_section_assignments(f) == [
    ...         ({2, 3, 4}, {6, 7, 8}),
    ...         ({2, 3}, {4, 5}),
    ...         ({5, 6, 7}, {7, 8, 9}),
    ...         ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
    ...         ({6}, {4, 5, 6}),
    ...         ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8})
    ...     ]
    True
    """

    def _str_to_assignment(s: str) -> SectionAssignment:
        start, end = map(int, s.split("-"))
        return set(range(start, end + 1))

    def _str_to_assignments_list(line: str) -> SectionAssignmentPair:
        a, b, *_ = line.strip().split(",")
        return (_str_to_assignment(a), _str_to_assignment(b))

    return [_str_to_assignments_list(line) for line in file_in]


if __name__ == "__main__":
    main()
