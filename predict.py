from __future__ import division
import fasttext

classifier = fasttext.supervised('ransomware_text_train.txt', 'model', label_prefix='__label__')
fname="ransomware_text_test.txt"

outTrue = []

with open(fname) as f:
	content = f.readlines()
 
for test_twts in content:
	outTrue.append(test_twts.split(" ")[0][9:])

# print len(outTrue)
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
labels = classifier.predict(content)

outPred = [label[0] for label in labels]

relevant_correctness = 0
relevant_incorrectness = 0
irrelevant_correctness = 0
irrelevant_incorrectness = 0

for i,j in zip(outPred, outTrue):
	print i,j
	if i == "relevant" and j == "relevant":
		relevant_correctness += 1    
	if i == "irrelevant" and j == "relevant":
		relevant_incorrectness += 1
	if i == "irrelevant" and j == "irrelevant":
		irrelevant_correctness += 1    
	if i == "relevant" and j == "irrelevant":
		irrelevant_incorrectness += 1


print(relevant_correctness, relevant_incorrectness, irrelevant_correctness, irrelevant_incorrectness)
print("Relevant Accuracy: {:.6}".format(relevant_correctness / (relevant_correctness + relevant_incorrectness)))
print("Irrelevant Accuracy: {:.6}".format(irrelevant_correctness / (irrelevant_correctness + irrelevant_incorrectness)))

precision = relevant_correctness / (relevant_correctness + irrelevant_incorrectness)
print("Precision: {:.6}".format(precision))

recall = relevant_correctness / (relevant_correctness + relevant_incorrectness)
print("Recall: {:.6}".format(recall))

F1 = 2 * precision * recall / (precision + recall)
print("F1 score: {:.6}".format(F1))

print("Accuracy: {:.6}".format((relevant_correctness + irrelevant_correctness) / (relevant_correctness + relevant_incorrectness + irrelevant_correctness + irrelevant_incorrectness)))

