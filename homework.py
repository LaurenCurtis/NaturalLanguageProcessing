from os import write
from nltk.corpus.reader import wordnet
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

from wordcloud import WordCloud
import wordcloud
wordcloud = WordCloud().generate(str(top15))
wordcloud.to_file("John.png")
