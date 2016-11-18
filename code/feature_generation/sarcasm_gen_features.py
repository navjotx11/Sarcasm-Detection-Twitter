# Generate primary first level features
# (+ve word count) (-ve word count) (overall polarity) (times change in pol) (largest + cont) (largest - cont) (capital letters) (punctuation)
import re,csv
import codecs
f3 = codecs.open('../../data/sarcasm_tweets.txt', encoding='utf-8')
csvfile = open('../../data/sarcasm_gen_features.csv','wb')
csvwriter =csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# print('(+ve word count) (-ve word count) (overall polarity) (times change in pol) (largest + cont) (largest - cont) (capital letters) (punctuation)')
csvwriter.writerow(['(+ve word count) ','(-ve word count)' ,'(overall polarity)' ,'(times change in pol)' ,'(largest + cont)' ,'(largest - cont)' ,'(capital letters)' ,'(punctuation)'])
f2 = open('../../data/sarcasm_tweets_clean.txt')

pattern=re.compile(r'\[(\-?[0-9])\]')
capital_count=[]
punctuation_count=[]
q=0
for l in f3 :

    punctuation_count.append(l.count('!')+l.count('?'))
    for x in range(len(l)-2):
        if l[x]=='.' and l[x+2]=='.':
            punctuation_count[-1]=punctuation_count[-1]+1

# print len(punctuation_count)
for l,inde in zip(f2,range(len(punctuation_count))):
    t= l.split(' ')
    ls=[]
    for x in t :
        try:
            ls.append(int(pattern.findall(x)[0]))
        except:
            continue
    pc,nc=0,0
    lsp,lsn=[],[]

    lsp = list(filter(lambda(x):x>0 , ls ))
    lsn= list(filter(lambda(x):x<0 , ls ))

    change_pol,prev=0,0
    for x in ls :
        if(x==0):
            continue
        if(prev==0 and x>0):prev=1
        elif(prev==0 and x<0):prev=-1
        elif(x>0 and prev<0 or x<0 and prev>0):
            change_pol=change_pol+1
            prev=-1*prev


    neg_max,pos_max=0,0
    cur=0
    prev=0
    for x in ls :
        if(x==0):
            continue
        if(prev==0 and x>0):
            prev=1
            cur=1
        elif(prev == 0 and x<0):
            prev = -1
            cur = 1
        elif(x>0 and prev>0 or x<0 and prev<0):cur=cur+1
        elif(x>0 and prev<0 or x<0 and prev>0):
            if(prev<0):neg_max=max(neg_max,cur)
            else:pos_max=max(pos_max,cur)
            prev= -1*prev
            cur=1
    else:
        if(prev<0):neg_max=max(neg_max,cur)
        elif(prev>0):pos_max=max(pos_max,cur)


    capital_count.append(sum(list(map(lambda x : x.isupper(),list(l))))-l.count('NAME')*4 - l.count('HYPERLINK')*9)



    try:
        q+=1
        csvwriter.writerow([len(lsp),len(lsn),sum(lsp)+sum(lsn),change_pol,pos_max,neg_max,capital_count[-1],punctuation_count[inde]])
    except Exception as e:
        pass


csvfile.close()