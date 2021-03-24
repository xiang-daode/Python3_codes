# txt读
with open("dd.txt","r") as f:
    ftext = f.read()

# txt写
f = open('dd.txt', 'ab')
f = open('dd.txt', 'wb')
f.write('123')
f.close()
