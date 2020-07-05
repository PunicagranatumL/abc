import os
import sys
import dendropy

in_folder = sys.argv[1]
out_folder = sys.argv[2]

os.makedirs(out_folder)

file_num = len(os.listdir(in_folder))
print("Total ", file_num, " nexus files need to be converted")
print("Ready,go!")

for nex_file in os.listdir(in_folder):
    file_path = in_folder + "/" + nex_file
    file_pre = nex_file.split(".")[0]
    nex = dendropy.DnaCharacterMatrix.get(path=file_path,schema='nexus')
    out_file_path = out_folder + "/" + file_pre + ".fasta"
    nex.write(path=out_file_path,schema='fasta')

print("OK")




