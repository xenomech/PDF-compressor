import os




basedir=os.path.dirname(os.path.abspath(__file__))
orginalfiledir=os.path.join(basedir,"File to be compressed")


for root,dirs,files in os.walk(orginalfiledir):
    for file in files:
        if file.endswith("pdf"):
            path=os.path.join(root,file)
            label=os.path.basename(root).replace(' ','-').lower()
            print(label, path)
