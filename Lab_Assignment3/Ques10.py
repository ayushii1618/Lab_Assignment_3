from collections import Counter
import string

def most_repetitive_word(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        
        # Remove punctuation
        for punct in string.punctuation:
            text = text.replace(punct, '')
        
        words = text.split()
        if not words:  # empty file or no words
            return None, 0
        
        word_counts = Counter(words)
        
        # Get the most common word and its count
        most_common_word, count = word_counts.most_common(1)[0]
        return most_common_word, count

# Example usage
filename = "sample.txt"  # Replace with your file path
word, count = most_repetitive_word(filename)

if count > 0:
    print(f"The most repetitive word is '{word}' which appears {count} times.")
else:
    print("No words found in the file.")
