import pickle
import re
import preprocessor as p

rel_tweets = []
with (open("relevant.pkl", "rb")) as openfile:
    while True:
        try:
            rel_tweets.append(pickle.load(openfile))
        except EOFError:
            break

irrel_tweets = []
with (open("irrelevant.pkl", "rb")) as openfile:
    while True:
        try:
            irrel_tweets.append(pickle.load(openfile))
        except EOFError:
            break

fin_relevant = []
with open('outLabels.txt', 'a') as the_file:
	for tweets in irrel_tweets[0]:
		p.set_options(p.OPT.URL, p.OPT.EMOJI)

		# Remove URL EMOJI
		tweets = p.clean(tweets)
		text = tweets.lower()
		text = re.sub(r'#([\S]+)', r'\1', text, flags=re.I)
		text = re.sub(r'@([\S]+)', r'\1', text, flags=re.I)
		text = re.sub(r'cve[- ]?(\d+)[- ]?(\d+)', r'cve-\1-\2', text, flags=re.I)
		text = re.sub(r'ms[- ]?(\d+)[- ]?(\d+)', r'ms\1-\2', text, flags=re.I)
		text = text.rstrip()
		text = re.sub(r'[^\x00-\x7F]+',' ', text)
		#cleanTweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",cleanTweet).split())
		#cleanTweet = cleanTweet.rstrip()
		
		print("\n\n\n--------------------\n\n\n")

		the_file.write("__label__irrelevant " + (text) + '\n')