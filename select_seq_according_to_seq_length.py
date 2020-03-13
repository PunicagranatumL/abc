import sys
from Bio import SeqIO

inputfasta = sys.argv[1]
min_len = int(sys.argv[2])
outputfasta = sys.argv[3]

i = 0
j = 0

fw = open(outputfasta,'w')

for rec in SeqIO.parse(inputfasta,'fasta'):
	i += 1
	if len(rec.seq) > min_len:
		j += 1
		fw.write(">%s\n%s\n"%(rec.id,str(rec.seq)))
		
print("The total number of sequence is: ",i)
print("Number of sequence retained is: ",j)