import os
from pylovepdf.tools.compress import Compress


basedir=os.path.dirname(os.path.abspath(__file__))
orginalfiledir=os.path.join(basedir,"inputfile")
outputdir=os.path.join(basedir,"outputfile")


for root,dirs,files in os.walk(orginalfiledir):
    for file in files:
        if file.endswith("pdf"):
            path=os.path.join(root,file)
            label=os.path.basename(root).replace(' ','-').lower()
            print(label, path)


task = Compress('public_key', verify_ssl=True)
task.add_file(path)
task.set_output_folder(outputdir)
task.execute()
task.download()
task.delete_current_task()