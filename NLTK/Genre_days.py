import nltk
from nltk.corpus import brown

#Defining variables for genres and days. We only want to check categories 'news' and 'romance'.
genres = ['news', 'romance']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

cfd = nltk.ConditionalFreqDist((genre, word)
                               for genre in brown.categories()
                               for word in brown.words(categories=genre))

#cfd.tabulate(conditions=genres, samples=days)
cfd.plot(conditions=genres, samples=days)
