import os
import subprocess
import os
import sys

def compress(input_file_path, output_file_path, power="default"):
    initial_size = os.path.getsize(input_file_path)

    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dPDFSETTINGS={}'.format(power),
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    '-sOutputFile={}'.format(output_file_path),
                     input_file_path])
    final_size = os.path.getsize(output_file_path)
    print("Compressing")
    print("Creating Final file")
    print("Done.")


if __name__ == "__main__":
    basedir=os.path.dirname(os.path.abspath(__file__))
    orginalfiledir=os.path.join(basedir,"inputfile")
    outputdir=os.path.join(basedir,"outputfile")
    for root,dirs,files in os.walk(orginalfiledir):
        for file in files:
            if file.endswith("pdf"):
                path=os.path.join(root,file)
                label=os.path.basename(root).replace(' ','-').lower()
                print(label, path)
                outputfile=os.path.join(outputdir,file)
    compress(path,outputfile,"default")

