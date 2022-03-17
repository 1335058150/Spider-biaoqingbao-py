"""
@Project ：Spider 
@File    ：main.py
@Date    ：2022/3/16 14:31 
"""
# -*- coding: UTF-8 -*-
from Get_HTML.getit import askURL
from Get_HTML.re_find import re__
from Download.img import downloadimg
from conf.Conf import conf

if __name__ == '__main__':
    for i in range(conf.min_,conf.max_+1):
        # 获取到网页源码
        html = askURL(conf.urldemo + str(i))
        photo_url = re__(html=html,re_rule=conf.re_rule)
        header = conf.header
        for photo_url_ in photo_url:
            # print(photo_url_)
            # img = askURL(url=photo_url_, headers=header)
            if downloadimg(url=photo_url_,headers=header,targetpath=conf.targetpath) is None:
                continue
            else:
                print("Error")
                print("*"*30)