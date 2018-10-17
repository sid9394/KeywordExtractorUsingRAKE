from sklearn.feature_extraction.text import TfidfVectorizer
import re
import operator
import os
import glob
from nltk import word_tokenize
from nltk.corpus import stopwords
#
mypath = 'C:\\Users\\sidharth.m\\Desktop\\WikiData\\wikiremaining'

for root, dirs, files in os.walk(mypath):
     print("dirs---------",dirs)

     for name in dirs:
        print("name----",name)
        txtlink = os.path.join(mypath,name)

        for filename in glob.glob(os.path.join(txtlink, '*.txt')):
            print(filename)
            with open(filename, "r") as myfile:
                data = myfile.read().replace('\n', '')
# stop = set(stopwords.words('english'))
#
# print([ i for i in data.lower().split() if i not in stop])

tfidf = TfidfVectorizer()

response = tfidf.fit_transform([data])

feature_names = tfidf.get_feature_names()

for col in response.nonzero()[1]:
    print(feature_names[col], ' - ', response[0, col])





