import os
import subprocess
import os
import sys


basedir=os.path.dirname(os.path.abspath(__file__))
orginalfiledir=os.path.join(basedir,"inputfile")
outputdir=os.path.join(basedir,"outputfile")


for root,dirs,files in os.walk(orginalfiledir):
    for file in files:
        if file.endswith("pdf"):
            path=os.path.join(root,file)
            label=os.path.basename(root).replace(' ','-').lower()
            print(label, path)

