"""
Given a sequence of integers as an array, 
determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
Note: sequence a0, a1, ..., 
an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing."""


def solution(sequence):
    count = 0
    index = -1

    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            count += 1
            index = i

    if count > 1:
        return False
    if count == 0:
        return True
    if index == -1 or index == 1 or index == len(sequence) - 1 or sequence[index - 1] < sequence[index + 1] or sequence[index - 2] < sequence[index]:
        return True

    return False



