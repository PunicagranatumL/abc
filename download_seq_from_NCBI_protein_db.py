import os
import argparse
parser = argparse.ArgumentParser(description='This script was used to download gb or fasta file from NCBI protein database')
parser.add_argument('-f','--format',help='Please input file format you want to download',required=True)
parser.add_argument('-a','--accession',help='file name contain accession number of cp genome you want to download',required=True)
args = parser.parse_args()


fr = open(args.accession,'r')
acc = []
for line in fr:
	seqid = line.strip()
	if seqid not in acc:
		acc.append(seqid)

print(acc)
print("The number of sequence will be downloaded is: ",len(acc))

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "你的邮箱"

fold_name = "download_succcessfully"
os.mkdir(fold_name)
os.chdir(fold_name)

fw1 = open("output."+args.format,'w')
fw2 = open("../download_failed_ids.txt",'w')

failed_id = []
success_id = []

for line in acc:
	try:
		protein = Entrez.efetch(db='protein',id=[line],rettype=args.format)
		seq = SeqIO.read(protein,args.format)
		SeqIO.write(seq,fw1,args.format)
		success_id.append(line)
	except:
		fw2.write(line+"\n")
		if line not in failed_id:
			failed_id.append(line)

fw1.close()
fw2.close()
print(len(success_id),"sequence have been downloaded")


if len(failed_id) == 0:
	print("Congratulations")
	os.remove("../download_failed_ids.txt")
else:
	print(len(failed_id),"need to be downloaded again!","id was stored in download_failed_ids.txt")