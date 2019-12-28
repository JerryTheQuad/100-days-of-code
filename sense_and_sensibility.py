#Importing all the needed packages
import nltk
from nltk.book import *
from matplotlib import pyplot as plt
from nltk.corpus import stopwords

#Getting rid of stopwords
stop_words = set(stopwords.words('english'))

v = set(text2)
filtered_text2 = [w for w in v if not w in stop_words]

v_2 = len(filtered_text2)
v_3 = len(text2)

#Plotting the data
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
text_2 = ['Normal', 'Filtered']
word_number = [v_3, v_2]
ax.bar(text_2,word_number)
plt.show()
