import os
import sys
from Bio import SeqIO

inputFile = sys.argv[1]

fwLSC = open("LSC_region.fasta",'w')
fwIR = open("IR_region.fasta",'w')
fwSSC = open("SSC_region.fasta",'w')

for rec in SeqIO.parse(inputFile,'gb'):
	IR_pos = []
	for feature in rec.features:
		if feature.type == "repeat_region":
			for part in feature.location.parts:
				IR_pos.append(part.start)
				IR_pos.append(part.end)
	if len(rec.seq) == max(IR_pos):
		print(rec.id," 可以进行下一步分析！")
		IR_pos.sort()
		LSC = rec.seq[0:(IR_pos[0]-1)]
		IR = rec.seq[(IR_pos[0]-1):IR_pos[1]]
		SSC = rec.seq[IR_pos[1]:IR_pos[2]]
		fwLSC.write(">%s\n%s\n"%(rec.id,str(LSC)))
		fwIR.write(">%s\n%s\n"%(rec.id,str(IR)))
		fwSSC.write(">%s\n%s\n"%(rec.id,str(SSC)))
	else:
		fwLSC.close()
		fwIR.close()
		fwSSC.close()
		os.remove("LSC_region.fasta")
		os.remove("IR_region.fasta")
		os.remove("SSC_region.fasta")
		print(rec.id," 需要调整IR区域的相对位置！")
		break
if "LSC_region.fasta" in os.listdir():
	print("结果文件分别是：","LSC_region.fasta ","SSC_region.fasta ","IR_region.fasta ")
else:
	print("调整后重新注释再来提取！")