# Used to insert gaps in sarcasm_tweets.txt (required for certain codes)
import re
import codecs
import csv
fin = open('../../data/sarcasm_tweets.txt')
fout = open('../../data/sarcasm_tweets_gaps.txt','wb')

for l in fin:
	fout.write(l)
	fout.write('\n')
fout.close()

