# Combinedata from Sarcasm and Nonsarcasm files to 
# give it as input to the SVM classifier
import codecs
from random import shuffle
f1 = codecs.open('../../data/sarcasm_final_libsvm.txt', encoding='utf-8')
f2 = codecs.open('../../data/nonsarcasm_final_libsvm.txt', encoding='utf-8')
f3 = open('../../data/combined_libsvm.txt','w')
l=[]
for line in f1:
    l.append(line[:-3])

for lin in f2:
    l.append(lin[:-3])

shuffle(l)
for s in l:
    f3.write(s+'\n')