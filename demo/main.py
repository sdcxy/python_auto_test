# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import unittest


def add(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(add(2), 3)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = MyTest()
    s.test()
    print_hi('PyCharm')  # 打印Pycharm

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
