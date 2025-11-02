from functools import wraps

# task 1
def decorator(func):
    """decorator"""
    @wraps(func)
    def wrapper(t):
        func(t)
        print(func.__name__, f"({repr(t)})", sep='')
        f"({t})"
    # if we want to complement func's documentation
    wrapper.__doc__ = wrapper.__doc__ + " some more info"
    return wrapper

@decorator
def f(text):
    """some f() info"""
    print(text)

f('alpha')
help(f)

# task 2

def stop_words(words: list):
    def dec(func):
        def wrapper(x):
            text = func(x)
            for i in words:
                text = text.replace(i, "*")
            return text
        return wrapper
    return dec

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('nekto'))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# task 3

def arg_rules(type_: type, max_length: int, contains: list):
    def dec(func):
        def wrapper(arg):
            if type(arg) != type_:
                print('wrong type')
                return False
            elif max_length < len(arg):
                print('input is too big')
                return False
            for i in contains:
                if not i in arg:
                    print('you do not have necessary symbols')
                    return False
            else: return func(arg)
        return wrapper
    return dec



@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
