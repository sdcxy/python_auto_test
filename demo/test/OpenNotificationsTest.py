from appium import  webdriver
from excel.ReadExcel import *
import unittest

appium_data = get_xls_data("app_config.xls", "android")


class OpenNotificationsTest(unittest.TestCase):

    def test_open_message(self):
        driver = webdriver.Remote(appium_url, appium_data)
        driver.open_notifications()
        driver.back()


if __name__ == '__main__':
    OpenNotificationsTest.main()