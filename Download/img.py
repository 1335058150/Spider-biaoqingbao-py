"""
@Project ：Spider 
@File    ：img.py
@Date    ：2022/3/16 15:20 
"""
# -*- coding: UTF-8 -*-
import requests

def downloadimg(url, headers=None, targetpath=None, keynum=None):
    if url[0:4] != "http":
        return None
    if keynum is None:
        keynum = [22, 23]
    if targetpath is None:
        targetpath = "E:\\test\\"
    if headers is None:
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
        }
    r = requests.get(url, headers=headers)

    try:
        with open(targetpath + url[keynum[0]:], "wb") as f:
            f.write(r.content)
            print("已完成项目："+url)
            print("下载地址："+targetpath)
    except FileNotFoundError:
        try:
            with open(targetpath + url[keynum[1]:], "wb") as f:
                f.write(r.content)
                print("已完成项目："+url)
                print("下载地址："+targetpath)
        except FileNotFoundError:
            print("\033"+url + "出错")
            return url


