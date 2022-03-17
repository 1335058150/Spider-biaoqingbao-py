"""
@Project ：Spider 
@File    ：Conf.py
@Date    ：2022/3/17 13:42 
"""
# -*- coding: UTF-8 -*-

class conf:
    urldemo = "https://www.doutub.com/img_lists/new/"
    # 这边存放的是url爬取的极大值和最小值
    min_, max_ = (1, 35)
    # 这边的数据是使用的正则表达式
    re_rule = r'<img alt=".*?" src="(.*?)" data-v-39bd7a82>'
    # headers请求头
    header = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39",
        "Referer":
            "https://www.doutub.com/"
    }
    # 目标下载路径
    targetpath = "E://test1"

    # def __init__(self):
    #     # 这边放的应当是url除了末尾数字之外的其他部分
    #     self.urldemo = "https://www.doutub.com/img_lists/new/"
    #     # 这边存放的是url爬取的极大值和最小值
    #     self.min_,self.max_ = (1, 35)
    #     # 这边的数据是使用的正则表达式
    #     self.re_rule = r'<img alt=".*?" src="(.*?)" data-v-39bd7a82>'
    #     # headers请求头
    #     self.header = {
    #         "User-Agent":
    #             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39",
    #         "Referer":
    #             "https://www.doutub.com/"
    #     }
    #     # 目标下载路径
    #     self.targetpath = None

