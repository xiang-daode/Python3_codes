# 在这里写上你的代码 :-)
import os
# 默认位置: C:/Users/Administrator/mu_code/
cmd1 = "echo msgbox 12345679*36 > test123.vbs"
cmd2 = "echo ^<body bgcolor=#EE00AA^>^<marquee ^>A Fox running !^<^/marquee ^>^<^/body^> > test123.htm"
cmd3 = "echo print(765+123,'hello world') > test123.py"

os.system(cmd1)
os.system('test123.vbs')

os.system(cmd2)
os.system('test123.py')

os.system(cmd3)
os.system('test123.htm')
