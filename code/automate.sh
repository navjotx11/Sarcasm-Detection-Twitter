#!/bin/bash
echo Sarcasm Detection in tweets
cd feature_generation
echo Generating Features
python sarcasm_gen_features.py
python nonsarcasm_gen_features.py
python sarcasm_tweets_gap.py
cd ../../data
grep '[^[:blank:]]' < nonsarcasm_tweets.txt > nonsarcasm_tweets_nogap.txt
cd ../code/feature_generation
python sarcasm_gen_emojis.py 
python nonsarcasm_gen_emojis.py
Rscript combine_features_csv.R
echo Creating volcabulary for Unigrams
python create_vocab.py

cd ../neural_network
echo Training Neural Network!
python neural_network.py

cd ../svm
python nonsarcasm_final_features.py 
python sarcasm_final_features.py
python libsvm_data.py
python append_1.py
echo Training SVM Model!
python svm_classification.py
echo Finished!

