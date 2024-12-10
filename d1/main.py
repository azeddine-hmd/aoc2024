#!/usr/bin/env python3

import sys
import os.path
from typing import List


def main():
    # opening file input and parsing it
    if len(sys.argv) < 2:
        print('filename argument needed!')
        return
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print('File does not exist.')
        return
    left_list = []
    right_list = []
    with open(filename) as f:
        rows = f.read().splitlines()
        for row in rows:
            s = row.split()
            left_list.append(int(s[0]))
            right_list.append(int(s[1]))
    first_puzzle(list(left_list), list(right_list))
    second_puzzle(list(left_list), list(right_list))


def first_puzzle(left_list: List[int], right_list: List[int]):
    distances = []
    left_list.sort()
    right_list.sort()
    for i in range(len(left_list)):
        distances.append(abs(left_list[i] - right_list[i]))
    print(sum(distances))


def second_puzzle(left_list: List[int], right_list: List[int]):
    similarity_score = []
    for nbr in left_list:
        similarity_score.append(nbr * right_list.count(nbr))
    print(sum(similarity_score))


if __name__ == '__main__':
    main()
