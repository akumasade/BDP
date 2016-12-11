import cPickle as pickle
import sys
text_model = pickle.load(open("textModel.p", "rb"))

if len(sys.argv) > 1:
    n = int(sys.argv[1])
    for i in range(n):
        print "%s. \"%s\" \n" % (i+1, text_model.make_sentence(tries=100))
else:
    print "\"%s\" \n" % (text_model.make_sentence(tries=100))
