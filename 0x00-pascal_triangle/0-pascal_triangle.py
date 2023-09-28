#!/usr/bin/python3
""" implementation of Pascal's triangle """


def pascal_triangle(n):
    """ pascal's triangle function """
    
    grand_list = []
    
    if (n <= 0):
        return (grand_list)

    for i in range(n):
        grand_list.append(str(11**i))
    return (grand_list)
