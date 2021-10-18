from typing import Text
from textblob import TextBlob
from textblob.en.sentiments import NaiveBayesAnalyzer

text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)

"""print(blob.sentences)
print(blob.words)
print(blob.tags)
print(blob.noun_phrases)
print(round(blob.sentiment.polarity,3))
print(round(blob.sentiment.subjectivity,3))

for sentence in blob.sentences:
    print(sentence)
    print(round(sentence.sentiment.polarity,3))


text = "you are horrible"
blob = TextBlob(text)
print(blob)
print(round(blob.sentiment.polarity,3))

text = "you are the best"
blob = TextBlob(text)
print(blob)
print(round(blob.sentiment.polarity,3))
"""

from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)
for sentence in blob.sentences:
    print(sentence.sentiment)

spanish = blob.translate(to = 'es')
print(spanish)
chineese = blob.translate(to = 'zh')
print(chineese)
print(chineese.translate())
