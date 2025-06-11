
from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    print(f"{num_words} words found in the document")
    print(char_counts)

if __name__ == "__main__":
    main()

