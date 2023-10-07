#!/usr/bin/python3
""" implemenation of lockboxes """


def join(B, K):
    """ helper function """
    result = []
    for k in K:
        result += B[k]
    return result


def canUnlockAll(boxes):
    """ check all boxes """
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True
    return len(total) == len(boxes)
