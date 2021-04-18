#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   binstd.py
@Time    :   2021/04/18 16:38:53
@Author  :   Zzl
@Contact :   noaghzil@gmail.com
@Desc    :   从BINSTD数据源获取天气
'''

# here put the import lib
import json


def fetch_today_weather_data(date):
    f = open("../data.txt", "r", encoding="utf-8")
    data = json.load(f)
    return data
