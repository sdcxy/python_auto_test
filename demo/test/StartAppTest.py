import unittest
from excel.ReadExcel import *
from ddt import ddt, data
from appium import webdriver
import time

# 从表格获取数据
test_data = get_xls_data('app_config.xls', 'android')


"""
    
    1、获取设备名称： adb devices -l
        
    2、查看包名和activity： aapt dump badging D:\Smart_community-3.2.20210130160310_KINLONG.apk
        package: name='com.gemvary.phone.cloudcall'
        launchable-activity: name='com.gemvary.phone.cloudcall.LauncherActivity'
    3、appium 连接 启动app
"""


# 创建连接
def connect():
    return webdriver.Remote(appium_url, test_data)


# 全局定义
driver = connect()


# 打开设备进行拍照 录像
def open_devices():
    devices = test_data["devices"]

    def device_init():
        # 点击 进入设备页面
        driver.find_element_by_accessibility_id(dev).click()
        time.sleep(1)

    def play():
        # 连接视频
        driver.find_element_by_id("com.gemvary.phone.cloudcall:id/iv_vedio_play").click()
        time.sleep(15)

    def photo():
        # 拍照
        driver.find_element_by_id("com.gemvary.phone.cloudcall:id/tv_screen").click()
        time.sleep(2)
        # 保存
        driver.find_element_by_id("android:id/button1").click()
        time.sleep(2)

    def video():
        # 录像 开启
        driver.find_element_by_id("com.gemvary.phone.cloudcall:id/tv_record").click()
        # 录制10秒
        time.sleep(10)
        # 录像 关闭
        driver.find_element_by_id("com.gemvary.phone.cloudcall:id/tv_record").click()
        time.sleep(2)
        # 保存
        driver.find_element_by_id("android:id/button1").click()
        time.sleep(2)

    # 循环操作设备
    for dev in devices:
        # 进入设备页面
        device_init()
        # 打开视频流
        play()
        # 拍照
        photo()
        # 录像
        video()

        # 返回上一级
        driver.back()
        driver.back()


# 场景测试
def scene_test():
    # 切换到智能页面
    driver.find_element_by_id("com.gemvary.phone.cloudcall:id/fixed_bottom_navigation_container").click()
    # 循环执行场景


@ddt
class StartAppTest(unittest.TestCase):

    @data(test_data)
    def test_start(self, item):

        def permission_allowed():
            # 允许开启权限
            driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
            time.sleep(2)
            # 允许获取地址
            driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button").click()
            time.sleep(2)
            # 允许拍照媒体
            driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
            time.sleep(2)
            # 读取移动网络
            driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
            # 等待页面加载
            time.sleep(20)

        def login():
            # 登录
            texts = driver.find_elements_by_class_name("android.widget.TextView")
            # 遍历 文本为“输入账号登录”
            for i in texts:
                if i.text == '输入账号登录':
                    i.click()
                    break
            time.sleep(2)
            # 勾选
            driver.find_element_by_id("com.gemvary.phone.cloudcall:id/cb_yinsi").click()
            time.sleep(2)
            # 输入账号
            telephone = driver.find_element_by_id("com.gemvary.phone.cloudcall:id/login_et_phonenumber")
            telephone.send_keys(item["telephone"])
            time.sleep(2)
            # 点击登录
            driver.find_element_by_id("com.gemvary.phone.cloudcall:id/login_bt_login").click()
            time.sleep(2)
            # 权限允许
            driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
            time.sleep(2)

        def select_space():
            # 选择空间
            driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView").click()
            time.sleep(2)
            driver.find_element_by_accessibility_id(item["spaceName"]).click()
            time.sleep(2)

        # 判断是否已经启动
        if item["is_start"] == 1:
            # 允许权限开启
            permission_allowed()
            # 登录
            login()
            # 切换指定空间
            select_space()
            # 测试打开设备
            open_devices()

        else:
            # 切换指定空间
            select_space()
            # 测试打开设备
            open_devices()


if __name__ == '__main__':
    StartAppTest.main()
