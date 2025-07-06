from stats import count_words
from stats import count_chars
import sys


def get_book_text(file):
    with open(file, 'r') as f:
        file_contents = f.read()
        return file_contents

    
def main():
    fpath = f"{sys.argv[1]}"
    a = get_book_text(fpath) 
    count_words(a)
    count_chars(a)
    
try:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    main()
except:
    print("Usage: python3 main.py <path_to_book>")
    raise sys.exit(1)

