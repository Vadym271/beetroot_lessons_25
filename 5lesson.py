import random as rnd

#task 1
guess = input("Enter your guess:")
num = rnd.randint(1, 10)
if guess == num: print("You guessed!")
else: print("You are wrong, correct number is", num)

#task 2
name = input("Enter your name:")
age = int(input("Enter your age:"))
print("Hello ",  name,  ", on your next birthday you’ll be ",  age+1,  " years", sep = "")

#task 3
input = input("Enter your word:")

for i in range(5):
    letters = list(input)
    rnd.shuffle(letters)
    word = ''.join(letters)
    print(word)
    i+=1
