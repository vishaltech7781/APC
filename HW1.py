text = input("Enter a paragraph: ")

# Split words
words = text.split()

# 1. Total words
print("Total words:", len(words))

# 2. Word frequency
freq = {}
for w in words:
    w = w.lower()
    freq[w] = freq.get(w, 0) + 1

print("Word frequency:", freq)

# 3. Top 3 frequent words
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("Top 3 words:", sorted_words[:3])

# 4. Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1

print("Total vowels:", count)
text = input("Enter a paragraph: ")

# Split words
words = text.split()

# 1. Total words
print("Total words:", len(words))

# 2. Word frequency
freq = {}
for w in words:
    w = w.lower()
    freq[w] = freq.get(w, 0) + 1

print("Word frequency:", freq)

# 3. Top 3 frequent words
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("Top 3 words:", sorted_words[:3])

# 4. Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1

print("Total vowels:", count)
