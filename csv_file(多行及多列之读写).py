import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    lt=[]
    for i in range(10):
        lt.append([i,5*i,chr(0x4eff+i^34)])
    writer.writerows(lt)

    for i in range(10):
        lt.append([10+i,5*i,chr(0x4eff+i^67)])
    writer.writerows(lt)


#import csv
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
