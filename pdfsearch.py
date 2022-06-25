from importlib.metadata import files
from posixpath import basename
import pdfplumber
import filesearch
import os
import re
#pdf=pdfplumber.open("./python/pdfplumber/test.pdf")
#lt=pdf.pages[1].extract_text()
#print(lt)
#print(len(pdf.pages))
#
#os.chdir("./python/pdfplumber")]
def init_filepath(path):
    pdffiles=filesearch.filesearch(cur_dir=path,typename='pdf')
    return pdffiles
#print(pdffiles)
def single_pdf_search(key,filename):
    try:
        pdf=pdfplumber.open(filename)
    except:
        print("[pdf search]:error at opening "+filename+".pdf")
        return
    with open("tmp.txt","w",encoding="utf8") as f:
        for page in pdf.pages:
            content=page.extract_text()
            f.write(content)
    tar=open("tmp.txt","r",encoding="utf8")
    cts=tar.readlines()
    input_words=key
    words=input_words.split(' ')
    pat=[]
    matched=[]
    for key in words:
        pat.append('.*'+key+'.*')
        print(key,' ')
    print('')
    fg=0
    output_check=0
    print("[pdf search]:in file "+filename+".pdf")
    for txt in cts:
        fg=0
        for keypat in pat:
            match=re.match(keypat,txt)
            if match:
                fg+=1
            else:
                break
        if fg==len(pat):
            print(txt)
            output_check=1
    if output_check==0:
        print("No Matching content")
    tar.close()
    os.remove("tmp.txt")
    return
def pdf_search(key,path):
    pdffiles=init_filepath(path)
    for file in pdffiles:
        single_pdf_search(key,file)
if __name__=='__main__':
    key=input("input a key:")
    path=os.getcwd()
    print(path)
    pdf_search(key,path)
