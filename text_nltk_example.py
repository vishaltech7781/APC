import nltk
# import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')  # download tokenizer data

text = "Python is an amazing language. It is great for AI and Data Science!"

#breaking the text provided into the sentence
print("Sentences:", sent_tokenize(text))

# breaking the text provided into the words
print("Words:", word_tokenize(text))
