import requests
import struct
from onlineDuration import getDurationWithUrl


url1 = "https://www.jszsxy.com/sf-server/file/getFile/0-C_0/lbox/5a25db6693a74d209c9c69e8c46b82d0_0100/video/mp4/5a25db6693a74d209c9c69e8c46b82d0.mp4"
url2 = "https://www.jszsxy.com/sf-server/file/getFile/0-C_0/lbox/96db1828243840d5bcd4b1c5fb988ff0_0100/video/mp4/96db1828243840d5bcd4b1c5fb988ff0.mp4"
url3 = "https://www.jszsxy.com/sf-server/file/getFile/0-C_0/lbox/9ee5a4bcf4b64ce692c8980339f22427_0100/video/mp4/9ee5a4bcf4b64ce692c8980339f22427.mp4"
url4 = "https://www.jszsxy.com/sf-server/file/getFile/0-C_0/lbox/c646d292b9be46fc8c03fa13b3119dc3_0100/video/mp4/c646d292b9be46fc8c03fa13b3119dc3.mp4"
url5 = "https://www.jszsxy.com/sf-server/file/getFile/0-C_0/lbox/b57db408c04c48a68e86292015392d02_0100/video/mp4/b57db408c04c48a68e86292015392d02.mp4"

getDurationWithUrl(url2)
# s = struct.unpack('>I', b'\x00\x90\x08')
s = struct.unpack('>I', b'\x00\x01_\x90')
t = struct.unpack('>I', b'\n\x164\xe6')
duration = int(t[0] / s[0])
print(duration)
minutes = duration // 60
sec = duration % 60
res = "{:02d}:{:02d}".format(minutes, sec)
print(res)
print(len(b'\x00\x00\x00\x00\xe0\x93\xa3s\xe0\x93\xa3u\x00'))
print(len(b'\xa3u'))
# print(struct.unpack('>I', b'\x01f\x90\x08'))
# print(struct.unpack('>I', b'\x00\x00\x00\x5f'))
# print(struct.unpack('>I', b'\x00\x00\x00_'))
# print(struct.unpack('>I', b'\x00\x00\x011'))
# print(struct.unpack('>I', b'\x00\x00\x01\x31'))
# print(struct.unpack('>I', b'\x00\x00\x0af'))
# print(struct.unpack('>I', b'\x00\x00\x0a\x66'))
# print(struct.unpack('>I', b'\x11\xff\x90\x08'))
# print(struct.unpack('>I', b'\x00\x005-'))
# print(struct.unpack('>I', b'\x00\x00\x05-'))
# b'\x01_\x90\x08' <class 'bytes'>
# b'\xf1a\xa2\x00'
# (23040008,) (4049707520,)
# 02:55