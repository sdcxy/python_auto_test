# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from config.config import *
from utils.read_excel import read_g_module


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print(dir_path)
    g = read_g_module(config_path, 'g_gateway.xls')
    print(g)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


