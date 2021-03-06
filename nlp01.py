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
"""

from textblob import Word
index = Word('index')
print(index.pluralize())
cacti = Word('cacti')
print(cacti.singularize())

#wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

word = Word('theyr')
print(word.spellcheck())
print(word.correct())

word1 = Word('studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())
print(word1.lemmatize())
print(word2.lemmatize())

happy = Word('happy')
print(happy.definitions)
print(happy.synsets)

for s in happy.synsets:
    for l in s.lemmas():
        print(l.name)

synonym = happy.synsets[1].lemmas()[0].name()

antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name
print(antonym)