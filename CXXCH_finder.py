from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
input_file = raw_input('File with complete genomes: ')
path = input_file[0:string.rfind(input_file,'/')+1]
os.chdir(path)
records = SeqIO.parse(open(input_file,'rU'), 'fasta')
for record in records:
	print record.name
	print record.seq
#out_file = path + 'CXXCH_' + input_file[string.rfind(input_file,'/')+1:len(input_file)]
#output_handle = open(out_file,'w')
#SeqIO.write(sub_genomes,output_handle,'fasta')
#output_handle.close()