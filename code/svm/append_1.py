# Appending a '1' was required to make the code work
import re
import codecs
import csv
import random 
fin = open('../../data/combined_libsvm.txt')
fout = open('../../data/combined_libsvm_append_1.txt','wb')

for l in fin:
	a = l[:-1]
	fout.write(a+'1\n')
fout.close()

