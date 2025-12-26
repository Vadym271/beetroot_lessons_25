import random
import time

################################################## task 1 #################################################
def bubble_2dir(unsorted: list):
    swap = True
    up = True
    l = len(unsorted)
    while swap:
        if up:
            k = 0
            for i in range(l - 1):
                if unsorted[i] > unsorted[i+1]:
                    a = unsorted[i]
                    unsorted[i] = unsorted[i+1]
                    unsorted[i + 1] = a
                    k+=1
            if k == 0:
                swap = False
            up = False
        else:
            k = 0
            for i in range(-1, -l, -1):
                if unsorted[i - 1] > unsorted[i]:
                    a = unsorted[i]
                    unsorted[i] = unsorted[i - 1]
                    unsorted[i - 1] = a
                    k += 1
            if k == 0:
                swap = False
            up = True
    return unsorted

my_list = [5, 3, 4, 2, 1, 22]
print(bubble_2dir(my_list))

################################################## task 2 #################################################
def merge_sort(unsorted):
    def merge(list1, list2):
        result = []
        l1, l2 = len(list1), len(list2)
        while True:
            if l1 == 0:
                if list2[0] > result[-1]:
                    return result + list2
                if list2[-1] < result[0]:
                    return list2 + result

            if l2 == 0:
                if list1[0] > result[-1]:
                    return result + list1
                if list1[-1] < result[0]:
                    return list1 + result

            if list1[0] >= list2[0]:
                result.append(list2[0])
                list2.pop(0)
                l2 -= 1
            else:
                result.append(list1[0])
                list1.pop(0)
                l1 -= 1

    l = len(unsorted)
    i = l // 2

    if l == 1:
        return unsorted

    half1 = unsorted[:i]
    half2 = unsorted[i:]

    sorted1 = merge_sort(half1)
    sorted2 = merge_sort(half2)

    return merge(sorted1, sorted2)

print(merge_sort(my_list))

################################################## task 3 #################################################
def quick_sort(unsorted):
    if len(unsorted) == 1:
        return unsorted
    if len(unsorted) == 0:
        return []

    pivot = unsorted[-1]
    half1 = [i for i in unsorted if i < pivot]
    half2 = [i for i in unsorted if i > pivot]

    sorted_half1 = quick_sort(half1)
    sorted_half2 = quick_sort(half2)

    return sorted_half1 + [pivot] + sorted_half2

my_list = [2, 23, 11, 6, 87, 22, 0, 90]
print(quick_sort(my_list))

def insertion_sort(unsorted: list):
    l = len(unsorted)
    for i in range(1, l):
        sub_array = unsorted[0:i]
        a = unsorted[i]
        boundaries = False

        if a < sub_array[0]:
            unsorted.insert(0, a)
            unsorted.pop(i + 1)
            boundaries = True
        if a > sub_array[-1]:
            boundaries = True

        if not boundaries:
            found = False
            j = 0
            while not found:
                if a > sub_array[j] and a < sub_array[j + 1]:
                    unsorted.pop(i)
                    unsorted.insert(j + 1, a)
                    found = True
                j += 1

    return unsorted

# my_list = [2, 23, 11, 6, 87, 22, 0, 90]
# print(insertion_sort(my_list))

def quicksort_improved(unsorted, partition = 10):
    if len(unsorted) == 1:
        return unsorted
    if len(unsorted) == 0:
        return []
    if len(unsorted) < partition:
        return insertion_sort(unsorted)

    pivot = unsorted[-1]
    half1 = [i for i in unsorted if i < pivot]
    half2 = [i for i in unsorted if i > pivot]

    sorted_half1 = quick_sort(half1)
    sorted_half2 = quick_sort(half2)

    return sorted_half1 + [pivot] + sorted_half2

def test(limit, n=10000):
    arr = [random.randint(0, 10**6) for _ in range(n)]
    start = time.perf_counter()
    quicksort_improved(arr, partition=limit)
    return time.perf_counter() - start


limits = [0, 5, 10, 20, 50, 100, 200]

for l in limits:
    print(f"limit={l:3}: {test(l):.4f} s")
