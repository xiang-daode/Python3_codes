#coding = utf-8
from urllib.request import urlopen
import urllib
import re

with urlopen('https://cn.dreamstime.com/%E5%8A%A8%E7%89%A9-%E5%85%8D%E8%B4%B9%E5%BA%93%E5%AD%98%E7%85%A7%E7%89%87-image-free-860358') as response:
     for line in response:
         line = line.decode('utf-8')  # Decoding the binary data to text.

         #if '<title>' in line and '</title>' in line:  # look for tags
         #    print(line)

         if '<img src=' in line:  # look for tags
             print(line)