#Script for training a mymarkovify text model
# Run $ ipython -i Generator-train.py
# then use text_model.make_sentence(tries=100) to generate sentences
import nltk, mymarkovify
import extract
import numpy as np
import cPickle as pickle

# Directory from which we are going to train our model on

readfrom = "./twitter_samples"
#readfrom = "./ChopraEdited"
cleantext = extract.read(directory = readfrom)

#Looking at the size of our data set
stoken = nltk.tokenize.PunktSentenceTokenizer()
s = stoken.tokenize(cleantext)
print np.size(s), " sentences"

wtoken = nltk.tokenize.WordPunctTokenizer()
w = wtoken.tokenize(cleantext)
print np.size(w), " words"

#Train model
text_model = mymarkovify.Text(cleantext, state_size=3)

#save our trained model to a pickle file
pickle.dump(text_model, open("textModel.p", "wb"))
print "Done training. \n"
