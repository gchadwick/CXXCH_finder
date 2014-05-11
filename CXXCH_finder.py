from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import string
import re
import os
input_file = raw_input('Path to file with protein sequences to count CXXCHs (/Users/g/..): ')
path = input_file[0:string.rfind(input_file,'/')+1]
os.chdir(path)
records = SeqIO.parse(open(input_file,'rU'), 'fasta')
p = re.compile('c..ch',re.IGNORECASE)
for record in records:
	sequence = str(record.seq)
	if len(p.findall(sequence))>0:
		print record.name
		print record.seq
		print p.findall(sequence)
#out_file = path + 'CXXCH_' + input_file[string.rfind(input_file,'/')+1:len(input_file)]
#output_handle = open(out_file,'w')
#SeqIO.write(sub_genomes,output_handle,'fasta')
#output_handle.close()