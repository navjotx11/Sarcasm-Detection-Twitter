# We have used libsvm library for SVM classification
# Use appropriate paths for libsvm library 
# Input should in the proper format as specified by the libsvm library

import os
curr_dir = os.getcwd()
os.chdir(str(curr_dir) + '/libsvm-3.21/python')
from svmutil import *
from svm import *
y, x = svm_read_problem(str(curr_dir)+'/../../data/combined_libsvm_append_1.txt')
m = svm_train(y, x, '-c 4 -t 2')
p_label, p_acc, p_val = svm_predict(y, x, m)
p_actual=y
tp,fp,tn,fn=0,0,0,0
p_label=list(map(int,p_label))

for predicted,actual in zip(p_label,p_actual):
    if(predicted==actual and predicted==1): tp+=1
    elif(predicted==actual and predicted==0):tn+=1
    elif(predicted==0):fn+=1
    else:fp+=1

precision = float(tp)/(tp+fp)
recall = float(tp)/(tp+fn)
fscore = 2*precision*recall/(precision+recall)

print('Precision: ',precision)
print('Recall ',recall)
print('F-score: ',fscore)

os.chdir(curr_dir)
