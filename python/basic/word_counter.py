# Write a program to display the 3 most frequent words in a given text excluding articles and prepositions.

from collections import Counter
import string

def display_most_frequent_words(text):
    stop_words = ["a", "an", "the", "in", "on", "at", "to", "for", "of", "by", "with", "as", "this", "that", "these", "those", "and", "or", "but", "if", "is", "it"]
    words = text.lower().translate(str.maketrans("", "", string.punctuation)).split()
    words = [word for word in words if word not in stop_words]
    word_count = Counter(words)
    most_common = word_count.most_common(3)
    for word, count in most_common:
        print(f"{word}: {count}")

text = input("Enter the text: ")
display_most_frequent_words(text)