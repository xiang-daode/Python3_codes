import csv
import random


# ###################  生成数据,写入CSV文件  #######################
with open('大学规模表.csv', 'w', newline='') as csvfile:
    fieldnames = ['大学', '文科生','理科生','工科生']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    s3='大学'
    rnd=random
    for i in range(10):
        s1 = chr(0x4e00 + i )
        s2 = chr(0x9fa5 - i )
        s=s1+s2+s3
        v1=rnd.randint(1000,5000)
        v2 = rnd.randint(1000, 5000)
        v3 = rnd.randint(1000, 5000)
        writer.writerow({'大学':s, '文科生':v1,'理科生':v2,'工科生':v3})
    print('大学规模表.csv---已经生成')

# ###################  读取CSV文件,统计与按学科人数排序  #######################
#import csv
with open('大学规模表.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     k=0
     fieldnames = ['大学', '文科生', '理科生', '工科生']
     print(fieldnames)
     lt1,lt2,lt3=[],[],[] #三学科
     LT=[] #总体
     for row in reader:
         k+=1
         #print(k,row['大学'], row['文科生'],row['理科生'], row['工科生'])
         lt1.append(int(row['文科生']))
         lt2.append(int(row['理科生']))
         lt3.append(int(row['工科生']))
         LT.append([k,row['大学'],int(row['文科生']),int(row['理科生']),int(row['工科生'])])
     #=========== 常用统计 ============
     print('每学科人数:',sum(lt1),sum(lt2),sum(lt3))
     print('总人数:', sum(lt1)+sum(lt2)+ sum(lt3))
     print('每大学每学科人数均值:',sum(lt1)/k, sum(lt2)/k, sum(lt3)/k)
     #按'工科生'数量从小到大排序输出:
     LT2=sorted(LT, key=lambda LT: LT[4])
     for i in range(len(LT)):
        print(LT2[i])




