import unittest
from src.config.config import *
from src.utils.read_excel import *


class TestGModule(unittest.TestCase):

    @staticmethod
    def test_get_data():
        g = read_g_module(config_path, 'g_gateway.xls')
        assert hasattr(g, 'g_case_id')
        print('123')


if __name__ == '__main__':
    unittest.main()