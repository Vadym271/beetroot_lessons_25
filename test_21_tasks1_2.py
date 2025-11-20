import unittest
# tasks 1, 2


class MyContextManager:
    def __init__(self, file, mode = 'r'):
        self.file = file
        self.mode = mode
        self.file_obj = open(file, mode)
        self.counter = 0

    @staticmethod
    def log(message):
        with open('logged', 'a') as f:
            f.write(message + '\n')

    def __enter__(self):
        self.counter += 1
        MyContextManager.log(f'file opened {self.file} in mode {self.mode}')
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        MyContextManager.log(f'file closed {self.file}')
        if exc_type:
            MyContextManager.log(f'exception: {exc_val}')
        self.file_obj.close()

class TestManager(unittest.TestCase):
    man = MyContextManager("test.txt", "w")
    with man as f:
        f.write("hello")

    def test_write(self):
        with open("test.txt") as f:
            a = f.read()
        self.assertEqual(a, "hello")

    def test_counter(self):
        self.assertEqual(self.man.counter, 1)

    def test_logging(self):
        with open('logged') as f:
            a = f.readlines()
        self.assertEqual(a[-1].strip(), 'file closed test.txt')
if __name__ == '__main__':
    unittest.main()

