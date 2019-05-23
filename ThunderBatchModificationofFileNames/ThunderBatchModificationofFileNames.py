import os
path = 'D:\迅雷下载\苗疆蛊事艾宝良版120集全'

#读取文本文档中的文件地址，转换为文件名


#获取该目录下所有文件，存入列表中
f = os.listdir(path)

n = 0
for i in f:
    
    #设置旧文件名（就是路径+文件名）
    oldname = path + f[n]
    
    #设置新文件名
    newname = path + 'a' + str(n + 1) + '.JPG'
    
    #用os模块中的rename方法对文件改名
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    
    n+=1

