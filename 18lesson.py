import re
from functools import wraps
# task 1

class Emasils:
    def __init__(self, email):
        if not self.validate(email):
            raise ValueError('Invalid email')
        self.email = email

    @classmethod
    def validate(cls, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

my_email = Emasils('limd@gmail.com')

# task 2 ********************************************************

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self.workers = []

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError('your input is not Worker class')
        self.workers.append(worker)
        worker._boss = self

    def remove_worker(self, worker):
        if len(self.workers) != 0:
            self.workers.remove(worker)
        return



class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company
        self._boss = None
        self.boss = boss


    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        if (not isinstance(boss, Boss)) and (boss is not None):
            raise TypeError('your value is not Boss class')
        if self._boss is not None:
            self._boss.remove_worker(self)
        boss.add_worker(self)
        self._boss = boss



# створюємо босів
b1 = Boss(1, "John", "Microsoft")
b2 = Boss(2, "Sarah", "Google")

# створюємо працівників
w1 = Worker(101, "Mike", "Microsoft", b1)
w2 = Worker(102, "Anna", "Microsoft", b1)

# --- Assertions ---

# 1. Кожен працівник має босом саме Boss
assert isinstance(w1.boss, Boss)
assert isinstance(w2.boss, Boss)

# 2. Коли працівника створюємо, він автоматично додається до списку боса
assert w1 in b1.workers
assert w2 in b1.workers
assert len(b1.workers) == 2

# 3. Неможна встановити босом щось не-Boss
try:
    w1.boss = "not a boss"
    assert False, "TypeError was expected"
except TypeError:
    pass

# 4. Перепризначення боса має видаляти працівника зі старого боса
w1.boss = b2
assert w1 not in b1.workers
assert w1 in b2.workers

# 5. Список працівників боса містить тільки Worker, а не Boss
for worker in b2.workers:
    assert isinstance(worker, Worker)

# 6. Раніше список працівників в іншого боса не змінюється
assert w2 in b1.workers

# 7. Перепризначення боса не дублює працівників
w2.boss = b1
assert b1.workers.count(w2) == 1

# 8. Не дозволяється додавати в workers напряму (для цього setter і потрібен)
try:
    b1.workers.append("fake worker")
    assert False, "workers list must be protected from direct modification"
except Exception:
    pass

# ********************************** task 3 ***************************************

class TypeDecorators:
    @staticmethod
    def  to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            a = func(*args, **kwargs)
            try:
                return int(a)
            except:
                raise ValueError('expression cannot be converted to int')
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            a = func(*args, **kwargs)
            try:
                return bool(a)
            except:
                raise ValueError('expression cannot be converted to bool type')
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            a = func(*args, **kwargs)
            try:
                return str(a)
            except:
                raise ValueError('expression cannot be converted to string type')
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            a = func(*args, **kwargs)
            try:
                return float(a)
            except:
                raise ValueError('expression cannot be converted to float type')
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_nothing('25') == 25

assert do_something('True') is True
