 # given string
sentence=("phyton is fun")
words=sentence.split()
# Reversed the list of words
reversed_words= words[::-1]
# join the reversed list of words back into sentence
reversed_sentence= ' '.join(reversed_words)
print(reversed_sentence)