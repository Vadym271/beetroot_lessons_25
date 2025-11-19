#task 1
class Enumerator:
    def __init__(self, object, initial = 0):
        self.object = object
        self.length = len(object)
        self.index = initial

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        self.index+=1
        return (self.index - 1, self.object[self.index - 1])

mylist = Enumerator([1, 2, 3, 4, 5], 2)

for index, value in mylist:
    print(index, value, '\n')

#task 2

def in_range(start, end, step = 0):
    if start > end:
        step = -step
    else:
        step = step

    length = abs(start - end)
    while length > 0:
        yield start
        start += step
        length -= abs(step)

# for i in in_range(110, 10, 23):
#     print(i)

#task 3

class Iterate_on_numbers:
    """
    this iterator takes list of numbers and non-numbers, and iterates only on integers
    and returns squared number when [] called. if called element is non-integer it just returns it
    l = Iterate_on_numbers([2, 'a'])
    l[0] = 4
    l[1] = 'a'
    """
    def __init__(self, object):
        self.object = object
        self.index = 0
        self.length = len(object)

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < self.length:
            item = self.object[self.index]
            self.index += 1

            if isinstance(item, int):
                return item

        raise StopIteration

    def __getitem__(self, item):
        value = self.object[item]
        if isinstance(value, int):
            return value ** 2
        return value

l = Iterate_on_numbers([1, 2, '33', 3, 'adad', 'adad'])
for i in l:
    print(i)

print(l[0])
