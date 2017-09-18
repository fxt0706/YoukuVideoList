import requests
import json
from pprint import pprint


def run():
    # delete the '#' below if you need to do something test with json
    # and add the '#' for the second url
    # url = 'http://oagwezixg.bkt.clouddn.com/youku_test.json'
    url = 'https://api.youku.com/videos/by_me.json'

    # replace your private parameter below
    payloads = {'client_id':'99******ad*b','access_token':'62*****70**36****5c9ff'}
    youku_json_get = requests.get(url,params=payloads).json()

    # set the JSON data
    youku_json = json.dumps(youku_json_get)
    youku_text = json.loads(youku_json)

    # init the parameter for analysis and output
    video_num = len(youku_text['videos']) - 1  # return the length of dict -- nums of videos
    video_list = []
    file_times = open("youku_video_times.txt","wb")
    file_video = open("youku_video_list.txt","wb")

    # get the video list
    add_video_list(video_list,youku_text,video_num)

    # analyze the video times and output to .txt
    video_set = set(video_list)
    for item in video_set:
        if(video_list.count(item) > 1):
            # print(" %s : %d \n" % (item, video_list.count(item)))
            words = "%s : %d \n" % (item, video_list.count(item))
            file_times.write(words.encode('utf-8'))

    # get the final list of video(without the number of occurrences) and list
    video_list_final = sorted(video_set,key = video_list.index)
    # print(video_list_final)
    for item in video_list_final:
        words = item + "\n"
        file_video.write(words.encode('utf-8'))

    # close the file
    file_times.close()
    file_video.close()
    print("Get the video list succeed! \nCheck the two txt files for details")

def add_video_list(video_list,list_text,num):
    for i in range(num):
        video_list.append(list_text['videos'][i]['title'])

run()