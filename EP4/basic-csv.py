import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist)

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data

read = readcsv()
print(read)

#data = ['น้ำเต้าหู้',8,'10:00 น.']
#writecsv(data)
