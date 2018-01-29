from __future__ import division
import csv
import pickle
import re
import preprocessor as p
from gensim import models
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
import csv
import pickle
import re
import preprocessor as p

rel_tweets = []
irrel_tweets = []

with (open("/home/hridoy/Work/Ransomware/Old/ransomware-project/fastText/relevant.pkl", "rb")) as openfile:
    while True:
        try:
            rel_tweets.append(pickle.load(openfile))
        except EOFError:
            break

with (open("/home/hridoy/Work/Ransomware/Old/ransomware-project/fastText/irrelevant.pkl", "rb")) as openfile:
    while True:
        try:
            irrel_tweets.append(pickle.load(openfile))
        except EOFError:
            break


def preprocess(text: str):
    text = text.lower()

    text = re.sub(r'#([\S]+)', r'\1', text, flags=re.I)
    text = re.sub(r'@([\S]+)', r'\1', text, flags=re.I)
    text = re.sub(r'cve[- ]?(\d+)[- ]?(\d+)', r'cve-\1-\2', text, flags=re.I)
    text = re.sub(r'ms[- ]?(\d+)[- ]?(\d+)', r'ms\1-\2', text, flags=re.I)
    text = ' '.join(text.splitlines())
    return text

rel_tweets = [tweet for tweet in rel_tweets[0]]
irrel_tweets = [tweet for tweet in irrel_tweets[0]]

relevant_train, relevant_test = train_test_split(rel_tweets,
                                                     train_size=0.1,
                                                     test_size=0.9,
                                                     random_state=42)

irrelevant_train, irrelevant_test = train_test_split(irrel_tweets,
                                                     train_size=0.1,
                                                     test_size=0.9,
                                                     random_state=42)


print(len(relevant_train), len(relevant_test), len(irrelevant_train), len(irrelevant_test))
print("Relevant train length: {:,}".format(len(relevant_train)))
print("Relevant test length: {:,}".format(len(relevant_test)))
print("Relevant length: {:,}".format(len(rel_tweets)))
print()
print("Irrelevant train length: {:,}".format(len(irrelevant_train)))
print("Irrelevant test length: {:,}".format(len(irrelevant_test)))
print("Irrelevant length: {:,}".format(len(irrel_tweets)))

print 

tweets = rel_tweets + irrel_tweets
print("Tweets length: " + str(len(tweets)))

the_file = open("ransomware_text_train.txt","a")

the_file2 = open("ransomware_text_test.txt","a")

for tweets in relevant_train:
	t = preprocess(tweets)
	t = "__label__relevant " + str(t)
	the_file.write(t + '\n')

for tweets in irrelevant_train:
	t = preprocess(tweets)
	t = "__label__irrelevant " + str(t)
	the_file.write(t + '\n')

for tweets in relevant_test:
	t = preprocess(tweets)
	t = "__label__relevant " + str(t)
	the_file2.write(t + '\n')

for tweets in irrelevant_test:
	t = preprocess(tweets)
	t = "__label__irrelevant " + str(t)
	the_file2.write(t + '\n')

# for tweets in rel_tweets_test:
# 	p.set_options(p.OPT.URL, p.OPT.EMOJI)

# 	# Remove URL EMOJI
# 	tweets = p.clean(tweets)
# 	text = tweets.lower()
# 	text = re.sub(r'#([\S]+)', r'\1', text, flags=re.I)
# 	text = re.sub(r'@([\S]+)', r'\1', text, flags=re.I)
# 	text = re.sub(r'cve[- ]?(\d+)[- ]?(\d+)', r'cve-\1-\2', text, flags=re.I)
# 	text = re.sub(r'ms[- ]?(\d+)[- ]?(\d+)', r'ms\1-\2', text, flags=re.I)
# 	text = text.rstrip()
# 	text = re.sub(r'[^\x00-\x7F]+',' ', text)
	
# 	print("\n\n\n--------------------\n\n\n")

# 	the_file.write("__label__relevant " + (text) + '\n')


# for tweets in irrel_tweets_test:
# 	p.set_options(p.OPT.URL, p.OPT.EMOJI)

# 	# Remove URL EMOJI
# 	tweets = p.clean(tweets)
# 	text = tweets.lower()
# 	text = re.sub(r'#([\S]+)', r'\1', text, flags=re.I)
# 	text = re.sub(r'@([\S]+)', r'\1', text, flags=re.I)
# 	text = re.sub(r'cve[- ]?(\d+)[- ]?(\d+)', r'cve-\1-\2', text, flags=re.I)
# 	text = re.sub(r'ms[- ]?(\d+)[- ]?(\d+)', r'ms\1-\2', text, flags=re.I)
# 	text = text.rstrip()
# 	text = re.sub(r'[^\x00-\x7F]+',' ', text)
	
# 	print("\n\n\n--------------------\n\n\n")

# 	the_file.write("__label__irrelevant " + (text) + '\n')
