# Count emojis from tweers
# Count LOL, ROFL and LMAO

import re
import codecs
import csv
f = codecs.open('../../data/nonsarcasm_tweets.txt', encoding='utf-8')
count=[]
t=[]
laughexp=[]
for l in f:
    t.append(l)
    count.append(len(re.findall(u'[\U0001f600-\U0001f650]', l)))
    pat1=re.compile(r'(\blols?z?o?\b)+?',re.I)
    pat2=re.compile(r'(\brofl\b)+?',re.I)
    pat3=re.compile(r'(\blmao\b)+?',re.I)
    laughexp.append(len(re.findall(pat1,l)) + len(re.findall(pat2,l)) + len(re.findall(pat3,l)))
    try:
        next(f)
    except:
        break


# print(len(t)) 

with open('../../data/nonsarcasm_emoji.csv','w') as csvfile:
    x=csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    x.writerow(['emoji_count','laughter_exp_count'])
    for i in range(len(t)):
        x.writerow([count[i],laughexp[i]])

csvfile.close()
