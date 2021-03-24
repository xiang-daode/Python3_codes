import re

m = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m.groups())
#('24', '1632')

m = re.match(r"(\d+\.\d+)", "24.1632")
print(m.groups())
#('24.1632',)