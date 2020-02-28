import sys
from Bio import SeqIO

inputFile = sys.argv[1]
pos = int(sys.argv[2])

for rec in SeqIO.parse(inputFile,'fasta'):
	fw = open(rec.id+"_1.fasta",'w')
	seq_1 = rec.seq[0:pos]
	seq_2 = rec.seq[pos:]
	fw.write(">%s\n%s\n%s\n"%(rec.id,str(seq_2),str(seq_1)))
	
fw.close()
