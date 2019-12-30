#Importing all the needed packages and data
import nltk
from nltk.book import *
#Defining the 'percent' function to calculate the percent of a word usage in a text from NLTK
def percent(word, text):
    return 100 * text.count(word) / len(text)
