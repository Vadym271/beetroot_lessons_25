#task 1
class Person:
    def __init__(self, firstname, secondname, age):
        self.firstname = firstname
        self.secondname = secondname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.secondname} and I’m {self.age} years old")

person1 = Person('John', 'Doe', 27)
person1.talk()

person1.age = 132
person1.talk()

#task 2

class Dog:
    def __init__(self, age):
        self.age = age
    def human_age(self):
        return self.age * 7

my_dog = Dog(5)
print(my_dog.human_age())

# task 3
print('task3')
CHANNELS = ["BBC", "Discovery", "TV1000"]
class Remote:
    def __init__(self, list):
        self.channel = list[0]
        self.channels_list = list
        self.len = len(self.channels_list)

    def first_channel(self):
        self.channel = self.channels_list[0]
        return self.channel
    def last_channel(self):
        self.channel = self.channels_list[-1]
        return self.channel
    def turn_channel(self, N):
        try:
            self.channel = self.channels_list[N - 1]
            return self.channel
        except:
            print('there is no channel with this number')
    def previous_channel(self):
        if self.channel == self.channels_list[0]:
            self.channel = self.channels_list[-1]
            return self.channel
        else:
            index = self.channels_list.index(self.channel) - 1
            self.channel = self.channels_list[index]
            return self.channel
    def next_channel(self):
        if self.channel == self.channels_list[-1]:
            self.channel = self.channels_list[0]
            return self.channel
        else:
            index = self.channels_list.index(self.channel) + 1
            self.channel = self.channels_list[index]
            return self.channel
    def current_channel(self):
        return self.channel
    def exists(self, p):
        try:
            p = int(p)
            if (p > 0) & (p < self.len):
                return 'Yes'
            else:
                return 'No'
        except:
            if p in self.channels_list:
                return 'Yes'
            else:
                return 'No'

controller = Remote(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel() == "BBC"

assert controller.exists(4) == "No"

assert controller.exists("BBC") == "Yes"
