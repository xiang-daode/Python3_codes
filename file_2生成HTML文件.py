#生成100个文件:
for i in range(100):
    with open('f'+str(i)+'.html',"w") as f:
        f.write('<marquee>我不造'+str(i)+'病毒!</marquee>')
        f.write('<H1>病毒不是我造的</H1>')
        f.write('<hr>')
        f.write('<img src=img.png />')
