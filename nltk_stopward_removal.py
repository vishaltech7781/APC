import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')
#Removing common words like “the”, “is”, “and” that don’t add meaning.

text = "Python is very popular in data science and machine learning."

words = word_tokenize(text)
filtered_words = [w for w in words if w.lower() not in stopwords.words('english')]

print("Original Words:", words)
print("After Removing Stopwords:", filtered_words)
