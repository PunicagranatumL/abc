import argparse

from Bio import SeqIO

parser = argparse.ArgumentParser(description = 'This script was used to get mVISTA annotation file used to cp genome comparative analysis')
parser.add_argument('-i','--genbank',help="Please input genBank format file", required = True)
args = parser.parse_args()

fw = open(args.genbank + "_mVISTA_annotation","w")

for rec in SeqIO.parse(args.genbank,"gb"):
	for feature in rec.features:
		if feature.type == "gene":
			for part in feature.location.parts:
				if part.strand == -1:
					start_location = str(part.start+1)
					end_location = str(part.end)
					gene_name = feature.qualifiers["gene"][0]
					fw.write("<\t%s\t%s\t%s\n"%(start_location,end_location,gene_name))
				else:
					start_location = str(part.start+1)
					end_location = str(part.end)
					gene_name = feature.qualifiers["gene"][0]
					fw.write(">\t%s\t%s\t%s\n"%(start_location,end_location,gene_name))
		elif feature.type == "CDS":
			for part in feature.location.parts:
				if part.strand == -1:
					start_location = str(part.start+1)
					end_location = str(part.end)
					fw.write("%s\t%s\t%s\n"%(start_location,end_location,"exon"))
				else:
					start_location = str(part.start+1)
					end_location = str(part.end)
					fw.write("%s\t%s\t%s\n"%(start_location,end_location,"exon"))
		elif feature.type == "tRNA" or feature.type == "rRNA":
			for part in feature.location.parts:
				start_location = str(part.start+1)
				end_location = str(part.end)
				fw.write("%s\t%s\t%s\n"%(start_location,end_location,"utr"))
		else:
			print("%s %s"%(feature.type,"is not needed"))
			
print("The process is done!")

fw.close()		