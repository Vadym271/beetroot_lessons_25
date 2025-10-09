import random
import random as rnd

# task 1
len = 10
list = []
for i in range(len):
    list.append(rnd.random()*10)
max = 0
for i in range(len):
    if max < list[i]: max = list[i]
print(max)

# task 2
list1 = [random.randint(1, 10) for _ in range(10)]
list2 = [random.randint(1, 10) for _ in range(10)]
print(list1)
print(list2)
common = (set(list1) & set(list2))
print("common:", common)

# task 3
num = [i for i in range(101)]
i=0
num2 = []
while i < 100:
    if (num[i] % 7 == 0) & (num[i] % 5 != 0): num2.append(num[i])
    i+=1
print(num2)
