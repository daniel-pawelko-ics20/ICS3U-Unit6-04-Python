#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# 2D array

from random import randint


def average(arr: list):
    # variable
    total = 0

    # process/output
    for row in arr:
        for colm in row:
            total += colm
            print(colm, end=" ")
        print("")

    # return
    return total / (len(arr) * len(arr[0]))


def main():
    # main function for array

    # input
    rows = input("How many rows: ")
    rows = int(rows)
    colm = input("How many columns: ")
    colm = int(colm)

    # create array
    arr = [[randint(1, 50) for rand in range(colm)] for row in range(rows)]

    # output/process/calling function
    print(f"Average is {average(arr)}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
