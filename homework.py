from os import write
from textblob import TextBlob 
import nltk
from pathlib import Path 

from nltk.corpus import stopwords

stops = stopwords.words("english")


blob = TextBlob(Path("book of John text.txt").read_text())
more_stops = ["thy","ye","verily","thee","hath","say","thou","art","shall"]
stops += more_stops


items = blob.word_counts.items()

clean = [i for i in items if i[0] not in stops]
noun = [word for word in clean if word[0] in blob.noun_phrases ]
from operator import itemgetter 
sort = sorted(noun, key = itemgetter(1), reverse = True)

top15 = sort[:15]
print(top15)
import imageio
from wordcloud import WordCloud
import wordcloud

f = open("UpdateJohn.txt","w")
for i in noun:
    f.write(i[0])
f.close()