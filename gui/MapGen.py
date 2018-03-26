"""This is the Town Map Generator File."""

import random

"""Tiles have the option of being one of 5(?) types:
    0. Forest
    1. Grass
    2. River
    3. Pond
    4. Road
    5. House
"""


def main():
    """I think I need a main."""
    print("How many tiles would you like?")
    xSize = input("X: ")
    print(xSize)
    ySize = input("Y: ")
    print(ySize)
    genGrid(int(xSize), int(ySize))


def genGrid(xSize, ySize):
    """Function to generate the grid."""
    grid = [[random.randint(0, 5) for j in range(ySize)] for i in range(xSize)]

    print("\n")
    for i in range(xSize):
        for j in range(ySize):
            print(grid[i][j], end='')
            if j + 1 == ySize:
                print("\n", end='')


if __name__ == '__main__':
    main()
