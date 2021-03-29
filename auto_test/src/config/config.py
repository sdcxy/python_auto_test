#!/usr/bin/env python
# -*-coding:utf-8-*-
import os


""":type
    配置文件保存位置
"""
# 获取上级目录的绝对路径
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取配置文件的绝对路径
config_path = os.path.join(dir_path, 'excel')
