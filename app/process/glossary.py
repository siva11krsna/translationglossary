from nltk import *
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import string
import openpyxl

workbook = openpyxl.load_workbook('test BG.xlsx')
sheet = workbook.active
stop_words = set(stopwords.words('english'))
punctuations = set(string.punctuation)

wtw_dict = {}
english_words = []
nonenglish_words = []
def stem(word):
    suffix_list_1 = ["ing", "ed", "ly"]
    # ious is removed from the list as it leads to incorrect word...
    regexp = r'^(.*?)(ing|ly|ed|ies|ive|es|s|ment)?$'
    stemword, suffix = re.findall(regexp, word)[0]

    if wordnet.synsets(stemword):
        return stemword

    if suffix in suffix_list_1:
        stemword += "e"
        if wordnet.synsets(stemword):
            return stemword

    return word

def processText(text_input):
    token_words = word_tokenize(text_input)
    filtered_words = [word for word in token_words if
                      word.lower() not in (stop_words) and word.lower() not in (punctuations)]
    unique_words = list(set(filtered_words))

    for word in unique_words:
        if word not in english_words:
            if wordnet.synsets(word):
                stemword = stem(word)
                english_words.append(stemword)
            else:
                nonenglish_words.append(word)
def getGlossary():

    nltk.download('wordnet')

    delimiter_char = ";"

    for row in sheet.iter_rows():

        # process translation
        processText(row[4].value)

        # process purport
        if row[5].value is not None:
            processText(row[5].value)

        processText(row[3].value)

        # print(' word to word processing...> ', row[3].value)
        wtwList = row[3].value.split(delimiter_char)
        for tokenstr in wtwList:
            tokenstrings = tokenstr.split('–')
            valuewtw = tokenstrings.pop().strip()
            keywtw = tokenstrings.pop().strip()
            if keywtw in wtw_dict:
                if valuewtw not in wtw_dict[keywtw]:
                    wtw_dict[keywtw].append(valuewtw)
            else:
                wtw_dict[keywtw] = [valuewtw]

    print('word to word >> ')
    print(wtw_dict)
    print('english words >> ')
    print(english_words)
    print('non english words >> ')
    print(nonenglish_words)
getGlossary()