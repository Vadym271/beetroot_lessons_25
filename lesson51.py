# tasks 1,2 (lessons 28 homework with type hints)
import random
import time
from typing import List, Union

Numeric = Union[int, float]


def bubble_2dir(unsorted: List[Numeric]) -> List[Numeric]:
    swap: bool = True
    up: bool = True
    length: int = len(unsorted)

    while swap:
        k: int = 0
        if up:
            for i in range(length - 1):
                if unsorted[i] > unsorted[i + 1]:
                    unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                    k += 1
            if k == 0: swap = False
            up = False
        else:
            for i in range(-1, -length, -1):
                if unsorted[i - 1] > unsorted[i]:
                    unsorted[i], unsorted[i - 1] = unsorted[i - 1], unsorted[i]
                    k += 1
            if k == 0: swap = False
            up = True
    return unsorted


def quick_sort(unsorted: List[Numeric]) -> List[Numeric]:
    if len(unsorted) <= 1:
        return unsorted

    pivot: Numeric = unsorted[-1]
    half1: List[Numeric] = [i for i in unsorted[:-1] if i <= pivot]
    half2: List[Numeric] = [i for i in unsorted[:-1] if i > pivot]

    return quick_sort(half1) + [pivot] + quick_sort(half2)


def insertion_sort(unsorted: List[Numeric]) -> List[Numeric]:
    length: int = len(unsorted)
    for i in range(1, length):
        key: Numeric = unsorted.pop(i)
        j: int = i - 1
        while j >= 0 and unsorted[j] > key:
            j -= 1
        unsorted.insert(j + 1, key)
    return unsorted