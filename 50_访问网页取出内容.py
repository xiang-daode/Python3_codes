from urllib.request import urlopen
with urlopen('http://news.baidu.com/') as response:
     for line in response:
         line = line.decode('utf-8')  # Decoding the binary data to text.
         if '<title>' in line and '</title>' in line:  # look for tags
             print(line)
         if 'href' in line:  # look for tags
             print(line)    

