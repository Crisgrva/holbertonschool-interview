#!/usr/bin/python3
"""
0x01. Lockboxes
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
    """

    if type(boxes) is not list or not all(type(box) is list for box in boxes):
        return False

    lenBox = len(boxes)

    if lenBox == 0:
        return False

    if lenBox == 1:
        return True

    if not boxes[0] and lenBox > 1:
        return False

    unloking = {k: False for k in range(lenBox)}

    unloking[0] = True

    keys = [key for key in boxes[0]]

    while keys:
        newKey = []
        for key in keys:
            if key in unloking.keys() and unloking[key] is False:
                newKey += boxes[key]
                unloking[key] = True

        if all(unloking.values()) and len(unloking) == lenBox:
            return True

        keys = newKey
    return False
