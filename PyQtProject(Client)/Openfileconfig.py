#!/usr/bin/python -u
# -*- coding:cp936 -*-
class Openconfig():
    def __init__(self):
        pass
    def readfile(self,filepath):
        if filepath is not '' and filepath is not None:
            f = open(filepath)             # 返回一个文件对象
            line = f.readline()             # 调用文件的 readline()方法
            readdata=[]
            while line:
                print line,                 # 后面跟 ',' 将忽略换行符
                data=line.find('\n')
                data=line[0:data]
                #data=data.split(' ')
                readdata.append(data.split(' '))
                # print(line, end = '')　　　# 在 Python 3中使用
                line = f.readline()
            f.close()
            return readdata
    def addwrite(self,filepath,data):
         #f1 = open(filepath,'wb')
         if data is not '' or data is not None:
             f = open(filepath,'a')
             f.write(data)
             f.close()
    def resetwrite(self,filepath,data):
        if data is not '' and data is not None:
            f=open(filepath,'wb')
            usdata=''
            for i in range(len(data)):
                for j in range(len(data[i])):
                    if j==len(data[i])-1:
                      usdata=usdata+data[i][j]
                    else:
                      usdata=usdata+data[i][j]+' '
                usdata=usdata+'\n'
            f.write(usdata)
            f.close()