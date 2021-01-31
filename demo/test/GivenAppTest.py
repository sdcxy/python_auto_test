import unittest
from excel.ReadExcel import *
from ddt import ddt, data
from appium import webdriver
import time

# 从表格获取数据
config_data = get_xls_data('app_config.xls', 'android')


"""
    1、获取设备名称： adb devices -l

    2、查看包名和activity： aapt dump badging apk文件位置 D://Smart_community-3.2.20210130160310_KINLONG.apk
       package: name='com.gemvary.phone.cloudcall'
        launchable-activity: name='com.gemvary.phone.cloudcall.LauncherActivity'
    3、appium 连接 启动app
"""


# 创建连接
def appium_connect():
    return webdriver.Remote(appium_url, config_data)


class VideoDevice(object):

    def __init__(self, driver):
        self.driver = driver

    def connect(self, name):
        # 点击 进入设备页面
        self.driver.find_element_by_accessibility_id(name).click()
        time.sleep(2)

    def play(self):
        # 连接视频
        self.driver.find_element_by_id("com.gemvary.phone.cloudcall:id/iv_vedio_play").click()
        time.sleep(15)

    def photo(self):
        # 拍照
        self.driver.find_element_by_id("com.gemvary.phone.cloudcall:id/tv_screen").click()
        time.sleep(2)
        # 保存
        self.driver.find_element_by_id("android:id/button1").click()
        time.sleep(2)

    def video(self):
        # 录像 开启
        self.driver.find_element_by_id("com.gemvary.phone.cloudcall:id/tv_record").click()
        # 录制10秒
        time.sleep(10)
        # 录像 关闭
        self.driver.find_element_by_id("com.gemvary.phone.cloudcall:id/tv_record").click()
        time.sleep(2)
        # 保存
        self.driver.find_element_by_id("android:id/button1").click()
        time.sleep(2)


# 视频循环操作
def loop(driver):
    # 获取视频设备
    devices = config_data["devices"]
    video = VideoDevice(driver)
    # 循环操作设备
    for dev in devices:
        # 进入设备页面
        video.connect(dev)
        # 打开视频流
        video.play()
        # 拍照
        video.photo()
        # 录像
        video.video()
        # 返回上一级
        driver.back()
        driver.back()


class Given(object):

    def __init__(self, driver, params):
        self.driver = driver
        self.params = params

    # 权限允许
    def permission_allowed(self):
        # 允许开启拍照图片
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
        time.sleep(2)
        # 允许获取地址
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button").click()
        time.sleep(2)
        # 允许拍照媒体
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        time.sleep(2)
        # 读取移动网络
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        # 等待页面加载
        time.sleep(30)

    # 登录
    def login(self):
        # 登录
        texts = self.driver.find_elements_by_class_name("android.widget.TextView")
        # 遍历 文本为“输入账号登录”
        for i in texts:
            if i.text == '输入账号登录':
                i.click()
                break
        time.sleep(2)
        # 勾选
        self.driver.find_element_by_id("com.gemvary.phone.cloudcall:id/cb_yinsi").click()
        time.sleep(2)
        # 输入账号
        telephone = self.driver.find_element_by_id("com.gemvary.phone.cloudcall:id/login_et_phonenumber")
        telephone.send_keys(self.params["telephone"])
        time.sleep(2)
        # 点击登录
        self.driver.find_element_by_id("com.gemvary.phone.cloudcall:id/login_bt_login").click()
        time.sleep(2)
        # 权限允许
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        time.sleep(2)

    # 选择空间
    def select_space(self):
        # 选择空间
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(self.params["spaceName"]).click()
        time.sleep(2)


# 第一次打开app
def first_start(driver):
    given = Given(driver, config_data)
    # 允许权限
    given.permission_allowed()
    # 登录
    given.login()
    # 选择空间
    given.select_space()


# app 已开启在主页
def already_open_app(driver):
    given = Given(driver, config_data)
    # 选择空间
    given.select_space()


@ddt
class GivenAppTest(unittest.TestCase):

    @data(config_data)
    def test_check(self, item):
        driver = appium_connect()
        is_start = item["is_start"]
        if is_start == 0:
            already_open_app(driver)
        else:
            first_start(driver)
        loop(driver)


if __name__ == '__main__':
    GivenAppTest.main()
