import math
# task 1
def favorite_movie(movie):
    print(movie)
user_movie = input("enter your favourite movie: ")
favorite_movie(user_movie)

# task 2
def make_country(country, capital):
    print({country: capital})
    return {country: capital}
u_country, u_capital = input('enter country'), input('enter capital')
dict = make_country(u_country, u_capital)

# task 3
def make_operation(operator, *nums):
    if operator == '+': return sum(nums)
    if operator == '-': return 2*nums[0] - sum(nums)
    if operator == '*': return math.prod(nums)
print(make_operation('*', 5, 5, -10, -20))
