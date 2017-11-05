# YoukuVideoList

不稳定版本

## 使用前提

1. 申请了优酷视频开发者API
2. Python3 环境
3. 已安装 `requests` 库，若没有安装，执行 `pip3 install requests`

## 使用方法

填写 `config.py` 文件，修改 `youkuvideolist.py` 文件并执行。

执行完毕后会生成2个.txt文件以及1个.xls文件:

youku_video_times.txt ： 优酷的视频重复次数
youku_video_list.txt ： 单纯的视频列表（不重复）
youku_video_data.xls ： 所有的视频详细数据
