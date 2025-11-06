# task 1

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('woof woof woof')

class Cat(Animal):
    def  make_sound(self):
        print('meeeeeeeeeeeeeeow')

cat = Cat()
dog = Dog()

cat.make_sound()
dog.make_sound()

def f(animal):
    animal.make_sound()
f(cat)

# task 2
class Library:
    def __init__(self, books = None, authors = None):
        self.books = books if books is not None else {}
        self.authors = authors if books is not None else []

    def add_book(self, book, amount):
        if book in self.books.keys():
            self.books[book] = self.books[book] + amount
        else:
            self.books[book] = amount
            self.authors.append(book.author)

    def group_by_author(self, author):
        return author.authors_books(self)

    def group_by_year(self, year):
        return [i for i in self.books.keys() if year == i.year]

    def __str__(self):
        return "\n".join(f"{book}, amount: {amount}" for book, amount in self.books.items())
    def __repr__(self):
        return f"Book( \n {self.__str__()} \n )"
class Book:
    def __init__(self, book, author, year):
        self.book = book
        self.author = author
        self.year = year


    def __str__(self):
        return f"Title: {self.book}, author: {self.author.name}"
    def __repr__(self):
        return f"Book(Title: {self.book}, author: {self.author.name})"

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def authors_books(self, library):
        return [i for i in library.books.keys() if self == i.author]

    def __str__(self):
        return f"{self.name}, {self.birthday}. Born in {self.country}"
    def __repr__(self):
        return f"Author(name: {self.name}, birthday: {self.birthday}, country: {self.country})"


public_lib = Library()
orwell = Author('Orwell', 'England', '1907')
rowling = Author('Rowling', 'England', '1965')

orwell_book = Book('1984', orwell, 1949)
rowling_book= Book('Harry Potter', rowling, 1997)
rowling_book2 = Book('Cursed child', rowling, 2016)
public_lib.add_book(orwell_book, 4)
public_lib.add_book(rowling_book, 8)
public_lib.add_book(rowling_book2, 1)

print(public_lib.group_by_year(1997))

# task 3

class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __mul__(self, other):
        return Fraction(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Fraction(self.numer * other.denom, self.denom * other.numer)

    def __add__(self, other):
        if self.denom == other.denom:
            return Fraction(self.numer + other.num, self.denom)
        else:
            return Fraction(self.numer * other.denom + other.numer * self.denom, self.denom * self.numer)

    def __sub__(self, other):
        if self.denom == other.denom:
            return Fraction(self.numer - other.num, self.denom)
        else:
            return Fraction(self.numer * other.denom - other.numer * self.denom, self.denom * self.numer)

    def __str__(self):
        return f"{self.numer} / {self.denom}"

fraq1 = Fraction(1, 3)
fraq2 = Fraction(1, 2)

print(fraq1 * fraq2)
