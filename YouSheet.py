import pygsheets
import config

# 打开文件 读取行数 读取最后一行内容 写入内容 获得对应格子的值 列出所有内容

class YouSheet():

    def __init__(self):
        self.clinet = pygsheets.authorize()
        print(self.clinet)
        sh = self.clinet.open_by_key(config.LIST_WKS_ID)
        self.ws = sh.sheet1
        print(dir(self.ws))

    def append(self, value, row):
        self.ws.insert_rows(row, values=value, inherit=True)


    def list(self):
        print()

if __name__ == '__main__':
    run = YouSheet()



