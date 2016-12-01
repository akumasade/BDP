import nltk
import os, string, json, textract, mymarkovify
#import numpy as np

# Directory from which we are going to train our model on

default_dir = "./twitter_samples"
#default_dir = "./ChopraEdited"

def extract_chopra(path):
    """
    Function to extract all text from a file as a single string
    (Also removes non-ascii characters...supposedly)
    """
    
    #only reading from pdf files
    if path.endswith(".pdf"):
        text = textract.process(path, endcoding='ascii')
    else:
        pass
    
    text.replace("\n", " ")
    text.replace("\t", " ")
    text.replace("\s", " ")
    text.replace("\r", " ")
    filter(lambda x: x in set(string.printable), text)
    ' '.join(" " if ord(i)>128 else i for i in text)
    
    return text


def extract_tweets(path):
    """
    Function specifically made to read twitter_samples json files
    """
    dict_list = []
    
    for line in open(path):
        loaded = json.loads(line)
        dict_list.append(loaded)
        
    text = ""
    for item in dict_list:
        try:
            tweet = item["text"]
            filter(lambda x: x in set(string.printable), tweet)
            text += text
        except UnicodeEncodeError:
            pass
    
    return text



def read(directory = default_dir):
    # Extract texts as one big string (could change this later)
    alltext = ""

    print "Reading files..."
    for filename in os.listdir(directory):
        
        path = os.path.join(directory,filename)
        
        if (directory.find("twitter_samples") != -1 ) and filename.endswith(".json"):
            print path
            text = extract_tweets(path)
            alltext = alltext + ". " + text
        
        elif (directory.find("ChopraEdited") != -1) and filename.endswith(".pdf"):
            print path
            text = extract_chopra(path)
            alltext += " " + text
            


    print "Done Reading."

    """
    For some reason the ASCII filter didn't work,
    so now we're just manually removing the non-ASCII chars.
    """
    cleanstring = ""
    prev = 0
    for i,j in enumerate(alltext):
        if ord(j) > 128: 
            cleanstring += alltext[prev:i-1]
            prev = i+1
            
    return cleanstring #clean string for training




