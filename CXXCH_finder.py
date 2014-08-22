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
counter = 0
counter2 = 0
largest = 0
for record in records:
	counter2+=1
	sequence = str(record.seq)
	if len(p.findall(sequence))>0:
		print record.name
		print record.seq
		print 'number:',len(p.findall(sequence)), p.findall(sequence)
		if len(p.findall(sequence))>largest:
			largest = len(p.findall(sequence))
		counter+=1
print counter, 'of', counter2
print 'most CXXCHs:',largest
#out_file = path + 'CXXCH_' + input_file[string.rfind(input_file,'/')+1:len(input_file)]
#output_handle = open(out_file,'w')
#SeqIO.write(sub_genomes,output_handle,'fasta')
#output_handle.close()