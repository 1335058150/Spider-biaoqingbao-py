# Spider-biaoqingbao-py
针对一个表情包网站进行的爬虫程序（python）

## 第一次上传还请多多关照

## 使用注意事项

1. 首先请修改/conf/Conf.py文件下的一些列内容，这是源demo：
```python
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
```
2. 这里边的内容包括了URL模板，下载路径等信息。目前的1.0模板仅支持数字（GET请求）遍历网页。
3. 启动脚本，自动化执行
```sh
python main.py
```
