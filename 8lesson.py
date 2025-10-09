from collections import Counter
# task 1
something = input("write some sentence: ")
words = something.split(" ")
# method 1
uniq1 = Counter(words)
print(uniq1)
# method 2
set_words = list(set(words))
counts = [0 for _ in range(len(set_words))]
i = 0
j = 0
for i in range(len(set_words)):
    for j in range(len(words)):
        if set_words[i] == words[j]: counts[i]+=1
uniq2 = {set_words[i]: counts[i] for i in range(len(counts))}
print(uniq2)

# task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

keys = list(stock.keys())
total = {i: stock[i] * prices [i] for i in keys}
print(total)

# task 3
list_sq = [(i, i ** 2) for i in range(10)]
print(list_sq)

# task 4
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
dict1 = {i + 1: days[i] for i in range(len(days))}
dict2 = {days[i]: i + 1 for i in range(len(days))}
print(dict1)
print(dict2)
