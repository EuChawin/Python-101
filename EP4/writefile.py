def writedata(text):
    with open('data.txt','w',encoding='utf-8') as file:
        file.write(text)

def adddata(text):
    with open('data.txt','a',encoding='utf-8') as file:
        file.writelines(text + '\n')

def readdata():
    with open('data.txt',encoding='utf-8') as file:
        data = file.readlines()
        print(data)

#writedata('Hello world')
#adddata('Hello uncle')
readdata()
