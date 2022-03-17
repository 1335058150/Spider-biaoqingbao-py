"""
@Project ：Spider 
@File    ：re_find.py
@Date    ：2022/3/16 14:42 
"""
# -*- coding: UTF-8 -*-
import re

def re__(html: str, re_rule=None):
    if re_rule is None:
        return html
    else:
        rule = re.compile(re_rule)
        data = re.findall(rule, html)
        return data
