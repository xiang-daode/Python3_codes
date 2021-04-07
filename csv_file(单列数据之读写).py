import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(8):
        spamwriter.writerow([i,i+1,i+2,i+3])

    spamwriter.writerow(['Spam'] * 5 + ['\tBaked Beans'])
    spamwriter.writerow(['Spam', '\tLovely Spam', '\tWonderful Spam'])


#import csv
with open('eggs.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print(', '.join(row))
