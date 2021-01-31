from config.config import *
from xlrd import open_workbook


def get_devices(sheet):
    rows = sheet.nrows
    cls = []
    for i in range(1, rows):
        cls.append(sheet.row_values(i)[5])
    return cls


# 获取数据
def get_xls_data(xls_name, sheet_name):
    # 打开excel文件
    file = open_workbook(os.path.join(data_path, xls_name))
    # 读取sheet表
    sheet = file.sheet_by_name(sheet_name)
    # 获取参数
    platform_name = sheet.row_values(1)[0]
    device_name = sheet.row_values(1)[1]
    app_package = sheet.row_values(1)[2]
    app_activity = sheet.row_values(1)[3]
    is_start = sheet.row_values(1)[4]
    devices_name = get_devices(sheet)
    space_name = sheet.row_values(1)[6]
    telephone = sheet.row_values(1)[7]
    # 判断获取返回值
    if is_start == 1:
        return eval(str({
            "platformName": platform_name,
            "deviceName": device_name,
            "appPackage": app_package,
            "appActivity": app_activity,
            "is_start": is_start,
            "devices": devices_name,
            "spaceName": space_name,
            "telephone": telephone,
        }))
    else:
        return eval(str({
            "platformName": platform_name,
            "deviceName": device_name,
            "is_start": is_start,
            "devices": devices_name,
            "spaceName": space_name,
            "telephone": telephone,
        }))


if __name__ == '__main__':
    data = get_xls_data('app_config.xls', 'android')
    print(data)
