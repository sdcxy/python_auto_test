import os


"""
    xlsx文件的目录
"""
data_path = os.path.join(os.path.abspath('..'), 'data')
appium_url = "127.0.0.1:4723/wd/hub"


if __name__ == '__main__':
    print(data_path)