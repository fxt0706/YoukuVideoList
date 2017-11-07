# YoukuVideoList

不稳定版本
增加导出至 Google Sheet 功能
## 使用前提

1. 申请了优酷视频开发者API
2. Python3 环境
3. 已安装 `requests` 库，若没有安装，执行 `pip3 install requests`
4. Google Sheet 功能需要安装 `pygsheets` 库，若没有安装，执行 `pip3 install pygsheets`
5. Google Sheet 功能需要在 Google Developers Console 中打开 google spreadsheet api 以及 drive api 权限，**并将 `client_secret.json` 文件导出放入根目录**，详细步骤见此[链接](https://pygsheets.readthedocs.io/en/latest/authorizing.html)

## 本地版本使用方法

填写 `config.py` 文件，修改 `youkuvideolist.py` 中的时间参数，并执行 `python3 youkuvideolist.py`。

执行完毕后会生成2个.txt文件以及1个.xls文件:

youku_video_times.txt ： 优酷的视频重复次数
youku_video_list.txt ： 单纯的视频列表（不重复）
youku_video_data.xls ： 所有的视频详细数据

## Google Sheet 版本使用方法

完成 **试用前提** 中的第五步，并确保 `client_secret.json` 文件已在根目录。

在 Google Drive 中新建一个你需要导出的 Google Sheet 文件，范本如[这个文件](https://docs.google.com/spreadsheets/d/1-VX0obPVuCweJPkbTHqOe1c67fuEGf1qwBz4E9BwNn4/edit?usp=sharing)

填写 `config.py` 文件，其中 `LIST_WKS_ID` 为 Google Sheet 文件的 ID ，可在打开的网址中获取

修改 `youlistonline.py` 文件中的时间参数，并执行 `python3 youlistonline.py`

第一次运行时，会自动跳出浏览器，引导你进行授权。授权完成后，即可将数据导出到指定的 Sheet。