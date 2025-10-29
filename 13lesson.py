# task 1

def f():
    x = 2
    y = 1
    return x*y

def count_loc(func):
    return func.__code__.co_nlocals

print(count_loc(f))

# task 2
def f1():
    def f2():
        print('inner functions result')
    return f2

in_func = f1()
in_func()

# task 3

def choose_func(nums: list, func1, func2):
    if any(x < 0 for x in nums):
        return func2(nums)
    else:
        return func1(nums)


# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
