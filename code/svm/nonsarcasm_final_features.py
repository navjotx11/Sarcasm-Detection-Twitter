# Final feature generation for SVM
# This file will generate output in the format of libSVM
# Refer libSVM documentation for format

import re,csv
import codecs
from random import shuffle
flag = 0

f1 = codecs.open('../../data/nonsarcasm_tweets_nogap.txt', encoding='utf-8')
csvfile = open('../../data/nonsarcasm_final_features.csv','r')
f2=codecs.open('../../data/vocab.txt', encoding='utf-8')
f3 = open('../../data/nonsarcasm_final_libsvm.txt','w')
vocab={}
f4=csv.reader(csvfile, delimiter=' ')
for x in f2:
    x=x.rstrip('\n')
    id,word=x.split(':',1)
    vocab[word]=id
cnt=0
l10=[]
ind=0
for l1 in f4:
    l1=l1[0].split(',')
    l10.append(l1)

l10=l10[1:]
for l in f1:
    cnt=cnt+1
    words=l.split(' ')
    feature_dic ={}
    for word in words:
        try:
                id=vocab[word]
        except:
            continue
        try:
            feature_dic[id]=feature_dic[id]+1
        except:
            feature_dic[id]=1
    for i in range(10):
        feature_dic[i+1]=int(l10[ind][i])
        

    feature_list=[]
    ind+=1
    for key in feature_dic.keys():
        feature_list.append((int(key),feature_dic[key]))
    feature_list.sort(key=lambda tup:tup[0])
    f3.write('0 ')
    for x in feature_list:
        s=str(x[0])+':'+str(x[1])+' '
        f3.write(s)
    f3.write('\n')
# print(cnt)

