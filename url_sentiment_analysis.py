# Author: Endri Dibra

# Calling the required libraries
from textblob import TextBlob as tb
from textblob.sentiments import NaiveBayesAnalyzer
from newspaper import Article


# initializing url address, then as an article object
url = input("Please enter the url address")
article = Article(url)


# downloading article, parsing into it and preparing it for nlp
article.download()
article.parse()
article.nlp()


# summarizing article and analyzing it about its sentiment
# using Naive Bayes analyzer
text = tb(article.summary, analyzer=NaiveBayesAnalyzer())
print(text.sentiment)
