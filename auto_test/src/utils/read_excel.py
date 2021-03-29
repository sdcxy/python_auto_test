#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import xlrd


# G模块
class G_Module(object):
    def __init__(self, g_case_id, g_gateway_ip, g_gateway_port, g_riu_id, g_test_room_name, g_test_class_type, g_test_brand):
        self.g_case_id = g_case_id  # # 自动测试的用例ID
        self.g_gateway_id = g_gateway_ip  # 自动测试的主机IP
        self.g_gateway_port = g_gateway_port  # 自动测试的主机端口
        self.g_riu_id = g_riu_id  # 自动测试的网关类型
        self.g_test_room_name = g_test_room_name  # 自动测试的房间名
        self.g_test_class_type = g_test_class_type  # 自动测试的设备类型
        self.g_test_brand = g_test_brand  # 自动测试的设备品牌


# 读取G模块的配置 保存为G_Module
def read_g_module(dir_name, file_name):
    # 读取配置文件表格
    data = xlrd.open_workbook(os.path.join(dir_name, file_name))
    # 读取第一张表
    table = data.sheets()[0]
    # 读取第一张表的第二行数据的前7列
    g_module_data = table.row_values(1)[:8]
    # 封装到class G_Module
    g = G_Module(g_module_data[0], g_module_data[1], g_module_data[2], g_module_data[3], g_module_data[4], g_module_data[5], g_module_data[6])
    # 返回G模块类
    return g

