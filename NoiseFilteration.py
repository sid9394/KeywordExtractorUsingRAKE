import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    return cleantext

def get_filename(path):
    filename = re.findall("(?<=\-)(.*?)(?=\.)",path)
    return filename

def cleaningtxt(data):

    text = str(data)

    text1 = cleanhtml(text)
    text2 = str(text1)
    text3 = re.sub(r"\\t|\\r|\\n|\&n", "", text2)
    spremoval = re.sub('[^a-zA-Z0-9 \n\.]', '', text3)
    words = spremoval.split()
    return words
