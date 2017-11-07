import requests
import YouCore
from YouSheet import YouSheet
import config
import time


# file_times = open("./list/youku_video_times.txt","wb")
# file_video = open("./list/youku_video_list.txt","wb")
# xls_data = xlwt.Workbook()
# xls_table = xls_data.add_sheet('videos',cell_overwrite_ok=True)
xls_line = 2

# youku yun developer

class YouListOnline():

    def __init__(self, date = '1970-01-01'):
        print('YouList Message: Start output')

        time_now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        self.date = date + ' 23:59:59'
        self.sheet = YouSheet()

        url = config.URL_LIST_YUN

        # replace your private parameter below(client_id / access_token / video_page)
        payloads = {'client_id':config.CLIENT_ID_YUN,'access_token':YouCore.get_access_token_yun(),'count':50,'page':1}
        video_page = 2

        # get the JSON data and output to .xlsx
        video_list = []
        self.trans_json(video_page,video_list,url,payloads)

        # close the file
        print("Get the video list succeed! \nCheck the two .txt files and .xlsx file for details")


    def export_video_list(self,youku_text, num):
        #this function list the video to video_list and export details to .xls
        global xls_line

        for i in range(num):
            time_video = youku_text['videos'][i]['published']
            if self.compare_time(self.date, time_video) == False:
                value = []
                value.append(youku_text['videos'][i]['id'])
                value.append(youku_text['videos'][i]['title'])
                value.append(youku_text['videos'][i]['view_count'])
                value.append(youku_text['videos'][i]['link'])
                value.append(youku_text['videos'][i]['published'])
                self.sheet.append(value, xls_line)
                xls_line += 1
            elif self.compare_time(self.date, time_video) == False:
                break


    def trans_json(self,video_page,video_list,url,payloads):
        #this fuction get the all json files and deal with the data
        for i in range(1,video_page+1):
            youku_json_get = requests.get(url, params=payloads).json()
            video_num = len(youku_json_get['videos']) - 1    # the number of video in one json
            self.export_video_list(youku_json_get, video_num)
            payloads['page'] = i+1
            # time.sleep(0.9)


    def compare_time(self, time_std, time_video):
        time_std_struct = time.strptime(time_std, "%Y-%m-%d %H:%M:%S")
        time_video_struct = time.strptime(time_video, "%Y-%m-%d %H:%M:%S")
        return time_std_struct > time_video_struct



if __name__ == '__main__':

    YouListOnline()

    # if you need set the time use below like
    # YouListOnline('2017-10-1')




