"""
@Project ：Spider
@File    ：getit.py
@Date    ：2022/3/16 14:17
"""
# -*- coding: UTF-8 -*-
import requests

def askURL(url, headers=None):
    if headers is None:
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
        }
    try:
        req = requests.get(url=url,headers=headers)
        # 如果状态码错误
        if req.status_code >= 300:
            return None
        # 返回请求道的html网页源码
        return req.content.decode('utf-8')
    except:
        return None

