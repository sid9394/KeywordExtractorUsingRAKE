import textacy.keyterms
import SSGLog

logger = SSGLog.setup_custom_logger('Text-SpacyLogger_TagTest2')

with open('TextFilterSTEM.log', encoding = "utf-8") as myfile:
    data = myfile.read().replace('\n', '')
    text = str(data)
    doc = textacy.Doc(text)
    Sgrnk=textacy.keyterms.sgrank(doc, ngrams=(1,2,3,4,5,6), normalize='lower', n_keyterms=0.1)
    outlist = [(word, value) for words, value in Sgrnk for word in words.split()]
    print("Individual scores - ", outlist)
