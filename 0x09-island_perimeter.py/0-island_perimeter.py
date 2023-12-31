#!/usr/bin/python3
""" island perimeter algorithm """


def check_around(grid, i, j):
    """ check surroundings of a cell """
    perim = 0

    if grid[i][j-1] == 0:
        perim += 1
    if grid[i][j+1] == 0:
        perim += 1
    if grid[i-1][j] == 0:
        perim += 1
    if grid[i+1][j] == 0:
        perim += 1
    return perim


def island_perimeter(grid):
    """ calculate island perimeter """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += check_around(grid, i, j)

    return perimeter
