#打印不整齐数组:
import pprint


t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)

#按指定宽度输出文本:
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

#对各种字符进行排序:
import reprlib
a=reprlib.repr(set('supercalifragilistic,$expiali,#docious,456,111,999'))
print(a)


