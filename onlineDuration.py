import requests
import struct
from downloadDuration import xw_toExcel, getUrlName


def getDurationWithUrl(url):
    r = requests.get(url, stream=True)
    for data in r.iter_content(chunk_size=512):
        if data.find(b'mvhd') > 0:
            index = data.find(b'mvhd') + 4
            time_scale = struct.unpack('>I', data[index + 13:index + 13 + 4])
            durations = struct.unpack('>I', data[index + 13 + 4:index + 13 + 4 + 4])
            # 总时长，单位是秒
            duration = int(durations[0] / time_scale[0])
            minutes = duration // 60
            sec = duration % 60
            res = "{:02d}:{:02d}".format(minutes, sec)
            print(res)
            return res


def main():
    urlList, fileList = getUrlName("测试视频地址.txt")
    durationList = []
    for i in range(len(urlList)):
        dur = getDurationWithUrl(urlList[i])
        durationList.append(dur)
        print("第{}个已完成".format(i + 1))

    xw_toExcel(fileList, durationList, 'test.xlsx')
