#task1
class Stack:
    def __init__(self):
        self._list = []

    def push(self, item):
        self._list.append(item)

    def pop(self):
        return self._list.pop()

    def __len__(self):
        return len(self._list)

    def is_empty(self):
        return len(self._list) == 0

    def peek(self):
        return self._list[-1]
    #comments!!!!!!!!
    def is_balanced(self):
        """checks whether text has correct amount of braces in correct places.
        if at any point we encounter more opening braces than closing when unstacking it means that text is not balanced
        if we encounter uneven amount of opening and closing braces it means that text is not balanced"""
        internal_list = self._list
        #making list of only text's braces
        betabraces = [i for i in internal_list if i in '[]{}()']
        braces = Stack()
        if betabraces == []:
            print('there is no braces in your text')
            return
        for i in betabraces:
            braces.push(i)

        close_round = 0
        close_square = 0
        close_fig = 0
        while True:
            #checking for ()
            a = braces.pop()
            if a == ')':
                close_round += 1
            if a == '(':
                close_round -= 1

            #checking for []
            if a == ']':
                close_square += 1
            if a == '[':
                close_square -= 1

            #checking for {}
            if a == '}':
                close_fig += 1
            if a == '{':
                close_fig -= 1

            # checking if we encounter any opening braces without closing braces
            if close_fig < 0 or close_square < 0 or close_round < 0:
                return False
            if len(braces) == 0 and close_fig == 0 and close_round == 0 and close_square == 0:
                return True
            if len(braces) == 0:
                return False

    def get_from_stack(self, e):
        """ returns first instance of item in the stack"""
        help_stack = Stack()

        i = self.pop()
        try:
            while i != e:
                help_stack.push(i)
                i = self.pop()
            while len(help_stack) != 0:
                self.push(help_stack.pop())
            return e
        except IndexError:
            raise IndexError('there is no such item in your stack')

    def __str__(self):
        return "\n".join(self._list)

    def __reversed__(self):
        stack_reversed = Stack()
        for i in range(len(self._list)):
            stack_reversed.push(stack.pop())
        return stack_reversed

my_list = ['q', 'w', 'e', 'r', 't', 'y']
stack = Stack()
for i in my_list:
    stack.push(i)

stack_reversed = reversed(my_list)

print(stack_reversed)

#task 2
mylist2 = 'asdfrfv'
stack = Stack()
for i in mylist2:
    stack.push(i)

print(stack.is_balanced())

print(stack.get_from_stack('v'))
print(stack)
