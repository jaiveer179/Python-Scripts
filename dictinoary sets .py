from collections import defaultdict


text = input("Enter a Paragraph:")
def sample_text(text):
        text = file.read()
        return text
with open("sample.txt", 'r') as file:
    text = file.read()
    print(text)
    

import string

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words
from collections import defaultdict

def count_word_frequency(words):
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return word_count

def display_most_common_words(word_count, top_n=10):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    print("\nMost common words:")
    for word, count in sorted_words[:top_n]:
        print(f"{word}: {count}")
        print(f"{word}: {count}")


from random import sample
import string
from collections import defaultdict

# Function to preprocess text (remove punctuation, convert to lowercase)
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words

# Function to count word frequency using a dictionary
def count_word_frequency(words):
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return word_count

# Function to display the most common words
def display_most_common_words(word_count, top_n=10):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    print("\nMost common words:")
    for word, count in sorted_words[:top_n]:
        print(f"{word}: {count}")

# Main function
def main():
    # User input or file input
    choice = input("Do you want to enter text manually (M) or read from a file (F)? ").strip().upper()
    
    if choice == "M":
        text = input("Enter a paragraph of text: ")
    elif choice == "F":
        filename = input("Enter the filename (with extension): ")
        with open(filename, "r") as file:
            text = file.read()
    else:
        print("Invalid choice! Exiting program.")
        return

    # Process text and count word frequency
    words = preprocess_text(text)
    word_count = count_word_frequency(words)
    
    # Display most common words
    display_most_common_words(word_count)

# Run the program
if __name__ == "__main__":
    main()

 

 