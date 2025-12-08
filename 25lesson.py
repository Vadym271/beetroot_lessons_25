# task 1

from node import Node


class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, new):
        new_node = Node(new)
        if self.is_empty():
            self._head = new_node
            return

        current = self._head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def index(self, element):
        """as in every array count starts with 0
        if element is not found returns None"""

        if self._head is None:
            raise ValueError("linked list is empty")

        current = self._head
        i = 0
        while current is not None:
            if current.get_data() == element:
                return i
            else:
                i+=1
                current = current.get_next()
        else:
            return None

    def pop(self):
        if self._head is None:
            raise ValueError("linked list is empty")
        current = self._head
        previous = self._head
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        a = current.get_data()
        previous.set_next(None)
        return a

    def insert(self, index: int, value):
        """ index should be counted from 0"""
        if index > self.size():
            raise IndexError("input index is out of range")

        i = 0
        current = self._head
        while i != index - 1:
            i+=1
            current = current.get_next()

        node = Node(value)
        node.set_next(current.get_next())
        current.set_next(node)

    def slice(self, start: int, end: int):
        """includes starting element, but doesn't include end element
        indices start with 0"""
        if start < 0 or end > self.size():
            raise IndexError("index is out of range")

        new_list = UnsortedList()
        i = 0
        current = self._head
        while i != end:
            if i >= start:
                new_list.add(current.get_data())
            current = current.get_next()
            i+=1

        return new_list


    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

class Stack:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def push(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def pop(self):
        temp = self._head.get_data()
        self._head = self._head.get_next()
        return temp

    def __repr__(self):
        representation = "<Stack: "
        temp = self._head
        while temp is not None:
            representation += f"{temp.get_data()} "
            temp = temp.get_next()
        return representation + ">"


class Queue:
    def __init__(self):
        self._head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def pop(self):
        if self._head is None:
            raise ValueError("linked list is empty")
        current = self._head
        previous = self._head
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        a = current.get_data()
        previous.set_next(None)
        return a

    def __repr__(self):
        representation = "<Queue: "
        temp = self._head
        while temp is not None:
            representation += f"{temp.get_data()} "
            temp = temp.get_next()
        return representation + ">"

if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    my_list.append(2)
    print(my_list)
    # testing pop
    # print(my_list)
    # print(my_list.pop())
    # print(my_list)

    #CHEKING INSERT
    # my_list.insert(2, 3)
    # print(my_list)

    print(my_list.slice(2, 5))

    #checking work of Stack class
    # my_stack = Stack()
    # my_stack.push(2)
    # my_stack.push(2)
    # my_stack.push(12)
    # my_stack.pop()
    # print(my_stack)

    my_stack = Queue()
    my_stack.add(2)
    my_stack.add(2)
    my_stack.add(12)
    my_stack.pop()
    print(my_stack)
