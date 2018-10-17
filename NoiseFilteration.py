import re
import SSGLog
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from stemming.porter2 import stem
from nltk.stem.snowball import SnowballStemmer

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, ' ', raw_html)
  return cleantext


logger = SSGLog.setup_custom_logger('TextfilterSTEM')

with open('C:\\Users\\sidharth.m\\Desktop\\WikiData\\wikiremaining\\wiki1\\723-Argo Navis.txt', "r") as myfile:
    data = myfile.read()
    text = str(data)

    text1 = cleanhtml(text)
    text2 = str(text1)
    text3 = re.sub(r"\\t|\\r|\\n|\&n", "", text2)
    text4 = text3.replace('/', ' ')
    words = text4.split()
    # print(words)

    # #Stem1
    # text5 = [" ".join([stem(word) for word in sentence.split(" ")]) for sentence in words]
    # # print(text5)
    # text6 = ' '.join(text5)
    # logger.info(text6)

    # #Stem2
    # wordss = ' '.join(words)
    # st = LancasterStemmer()
    # text5 = st.stem(wordss)
    # print(text5)

    #Stem 3
    stemmer = SnowballStemmer("english")

    stemmed = [stemmer.stem(word) for word in words]
    text5 = ' '.join(stemmed)
    text6 = []
    for word in text5.split():
        # print(word)
        if word.endswith('i'):
            # print(word)
            word = word[:-1]
            # print(word)
            text6.append(word)
        else:
            text6.append(word)
    # print(text6)
    text6 = ' '.join(text6)
    logger.info(text6)



    # #Lemma
    # wnl = WordNetLemmatizer()
    # pos_tag(word_tokenize(text4))
    # text5=[]
    # for word, tag in pos_tag(word_tokenize(text4)):
    #     wntag = tag[0].lower()
    #     wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
    #     if not wntag:
    #         lemma = word
    #     else:
    #         lemma = wnl.lemmatize(word, wntag)
    #         text5.append(lemma)
    # text6 = ' '.join(text5)
    # logger.info(text6)