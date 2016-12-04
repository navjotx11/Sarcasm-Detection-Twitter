CS 725 : Foundations of Machine Learning
========================================

Course Project
-------------

--------------------------------------------
Sarcasm Detection in Tweets
--------------------------------------------

Authors:
--------
Navjot Singh 	130110071  
Kalpesh Patil 	130040019  
Ashwin Bhat 	13D070006  
Yash Bhalgat	13D070014  


--------------------------------------------

Folders/Files Provided:
-----------------------
- codes
	- feature_generation
	- neural_network
	- svm

- data
	- (stores intermediate data files)

-------------------------------------------------------------------------------------------------------------------------------

TO DO:
-----------------------

just run automate.sh present in /code
$ : ./automate.sh


------------------------------------------------------------------------------------------------------------------------------

The Flow :
-----------

The project proceeds in the following manner working through different codes and files present :

1. Use Senti-Strength tool on sarcasm_tweets.txt and nonsarcasm_tweets.txt to generate polarity scores for each word.  
-> Output: sarcsam_tweets_clean.txt and nonsarcasm_tweets_clean.txt are obtained.

2. Run sarcasm_gen_features.py and nonsarcasm_gen_features.py. These generate the numerical features as discussed in the report.
-> Output: sarcasm_gen_features.csv and nonsarcasm_gen_features.csv are obtained

3. Run sarcasm_tweets_gap.py as gaps in sarcasm_tweets.txt are to be removed to run 'x'_gen_emojis.py.
-> Output: sarcasm_tweets_gap.txt is obtained. 

4. Run both sarcasm_gen_emoji.py and nonsarcasm_gen_emojis.py
-> Output: sarcasm_emoji.csv and nonsarcasm_emoji.csv are obtained.

5. Merging in sarcasm_emoji.csv and sarcasm_gen_features.csv (and same for nonsarcasm) is required, this is done by the Rscript provided.
-> We are now done with producing our numerical features.

6. Run create_vocab.py to form a extract unigrams from sarcsam_tweets.txt and nonsarcasm_tweets.txt
-> Output: vocab.txt storing occurence of each unigram in our data. 

7. Run neural_network.py
-> Output: Return Precision,Accuracy and Recall values for NN

8. Run nonsarcsam_final_features.py and sarcasm_final_features.py to make LibSVM features
-> Output : sarcasm_final_libsvm.py sarcasm_final_libsvm.py

9. Run svm_classification.py
-> Output: Return Precision,Accuracy and Recall values for SVM

----------------------------------------------------------------------------------------------------------------------------------


Results:
--------

(Please refer to the report)

Github Repository : https://github.com/navisngh11/Sarcasm-Detection-Twitter

-----------------------------------------------------------------------------------------------------------------------------------
