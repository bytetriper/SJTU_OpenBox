import pdfplumber
import os
import re
defaultfile=['pdf','txt','xlsx']
def sortfile(files,typename,output=False):
    targetfiles=[]
    cnt=0
    for file in files:
        if len(file.split('.'))<=1:
            continue
        if file.split('.')[1]==typename:
            targetfiles.append(file)
            cnt+=1
    if output:
        if cnt==0:
            print("No "+typename+" file is founded!")
        else:
            print(str(cnt)+" "+typename+" file founded")
    print("Find "+typename+" files:")
    print(targetfiles)
    return targetfiles
def filesearch(cur_dir,op=0,typename='NA',output=False):
    if op:
        cur_dir=os.getcwd()
    files=os.listdir(cur_dir)
    ansfile=[]
    #print(sortfile(files,typename))
    if typename=='NA':
        if output:
            print("Filename not provided,loading default filenames:")
        for type in defaultfile:
            ansfile.append(sortfile(files,type,output))
    else:
        return sortfile(files,typename)
    return ansfile
if __name__=="__main__":
    print(filesearch(r'python\filesearch',output=True))