import excelsearch
import pdfsearch
import auto_check
import os
path=''
print("[reading config]")
with open("config.txt","r") as f:
    path=f.read()
if os.path.exists(path):
    print("path:"+path)
else:
    print("[reading config]:Cannot find path in config.txt")
    exit(0)
key=input("Input Key:")
SJTU_on=input("SJTU?(Input [On] if you handle all the configs):")
excelsearch.excel_search(key,path)
pdfsearch.pdf_search(key,path)
if SJTU_on=='On':
    auto_check.getInfo(key)