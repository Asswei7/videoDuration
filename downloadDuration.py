import os
import xlsxwriter as xw
import cv2
import requests
from tqdm import tqdm


# 根据文件，获取视频名称列表和视频网址列表
def getUrlName(filename):
    _urlList = []
    _fileList = []
    # 记录起始行和最后一行
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for i in range(len(data)):
            if i % 2 ==0:
                _fileList.append(data[i].strip('\n'))
            else:
                _urlList.append(data[i].strip('\n'))
    return _urlList, _fileList


# 下载MP4到本地
def downloadVideo(url, filename):
    res = requests.get(url, stream=True)
    total = int(res.headers.get('content-length', 0))
    with open("./测试视频文件夹/" + filename + '.mp4', 'wb') as file, tqdm(
            desc=filename,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in res.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


def getFileDuration(filename):
    file_time = 0
    cap = cv2.VideoCapture(filename)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num = cap.get(7)
        duration = int(frame_num / rate)
        minutes = duration // 60
        sec = duration % 60
        res = "{:02d}:{:02d}".format(minutes, sec)
        cap.release()
        return res
    else:
        return file_time


def getAllFiles(_dirName):
    return os.listdir(_dirName)


def xw_toExcel(_fileList, _durationList, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['序号', '视频名', '视频时长']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(_fileList)):
        insertData = [j + 1, _fileList[j], _durationList[j]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表


def main():
    # 1. 获取视频名称和地址
    # urlList, fileList = getUrlName("测试视频地址.txt")
    # 2. 下载到本地
    # for i in range(len(urlList)):
    #     downloadVideo(urlList[i], fileList[i])
    # 3. 获取本地视频时长列表
    fileName = getAllFiles('./测试视频文件夹/')
    duration = []
    for item in fileName:
        d = getFileDuration('./测试视频文件夹/' + item)
        duration.append(d)
    print(duration)
    # 4. 写入excel中
    xw_toExcel(fileName, duration, 'test.xlsx')


if __name__ == '__main__':
    main()

