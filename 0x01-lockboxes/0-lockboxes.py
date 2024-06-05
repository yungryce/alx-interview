#!/usr/bin/python3
# lockboxes


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    for k in range(1, len(boxes) - 1):
        unlocked = False
        for i in range(len(boxes)):
            unlocked = k in boxes[i] and k != i
            if unlocked:
                break
        if unlocked is False:
            return unlocked
    return True


"""
def canUnlockAll(boxes):
    x = len(boxes)
    item = [False] * x
    item[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for each in boxes[box]:
            if each >= 0 and each < x and not item[each]:
                item[each] = True
                stack.append(each)

    return all(item)
"""
