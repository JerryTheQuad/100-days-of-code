#Importing all the needed packages
import nltk
from nltk.tokenize import sent_tokenize

#Opening the file (the file path may differ)
f = open('/Users/valerij/Desktop/Onegin.txt')
raw = f.read()
#Tokenizing the raw file, giving the Python the taste of Pushkin's sentences
onegin = sent_tokenize(raw)
print(onegin[24])
