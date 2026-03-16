from nltk import *
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import string


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
            english_words.append(word)
        else:
            nonenglish_words.append(word)

    print('english words >> ', english_words)
    print('non english words >> ', nonenglish_words)
getGlossary()