import pandas as pd
import string
import regex as re
from pathlib import Path
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
nltk.download('punkt')
from nltk.corpus import stopwords

def html_remover(text):
    if isinstance(text,str):
        return re.sub(r"<.*?>","",text)
    return text

def punc_clean(text):
    pun=string.punctuation
    samp_tex=str()
    for i in text:
        if i not in pun:
            samp_tex += i 
    return samp_tex

def toke(text):
    tokens=word_tokenize(text)
    return tokens

def stop_word(text):
    stop_words=set(stopwords.words('english'))
    stop_words.remove('not')
    stop_words.remove('no')
    stop_words.remove('nor')
    filtered=[
        word for word in text
        if word.lower() not in stop_words
    ]
    return filtered

def lemmatization(lis):
    lemmatizer=WordNetLemmatizer()
    l=list()
    for word in lis:
        a=lemmatizer.lemmatize(word)
        l.append(a)
    return l



def preprocessing(text):
    text=html_remover(text)
    text=punc_clean(text)
    text=text.lower()
    text=toke(text)
    text=stop_word(text)
    text=lemmatization(text)
    text=" ".join(text)
    return text

if __name__=="__main__":
    preprocessing()
    