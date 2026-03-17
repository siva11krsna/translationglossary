from nltk import *
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import string

def stem(word):
    suffix_list_1 = ["ing", "ed", "ly"]
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stemword, suffix = re.findall(regexp, word)[0]

    if wordnet.synsets(stemword):
        return stemword

    if suffix in suffix_list_1:
        stemword += "e"
        if wordnet.synsets(stemword):
            return stemword

    return word

def getGlossary():

    nltk.download('wordnet')
    stop_words = set(stopwords.words('english'))
    punctuations = set(string.punctuation)

    translation = "Dhṛtarāṣṭra said: O Sañjaya, after my sons and the sons of Pāṇḍu assembled in the place of pilgrimage at Kurukṣetra, desiring to fight, what did they do?"

    translation_words = word_tokenize(translation)
    print(translation_words)
    filtered_words = [word for word in translation_words if word.lower() not in (stop_words) and word.lower() not in (punctuations)]
    print(filtered_words)
    unique_words = list(set(filtered_words))
    print(unique_words)

    english_words = []
    nonenglish_words = []

    for word in unique_words:
        if wordnet.synsets(word):
            stemword = stem(word)
            english_words.append(stemword)
            print(word, stemword)
        else:
            nonenglish_words.append(word)

    print('english words >> ', english_words)
    print('non english words >> ', nonenglish_words)
getGlossary()