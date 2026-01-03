import sys
from stats import get_num_words, get_num_char

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    count = get_num_words(content)
    chars = get_num_char(content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path + "...")
    print("----------- Word Count ----------")
    print("Found " + str(count) + " total words")
    print("--------- Character Count -------")
    for char in chars:
        print(char + ": " + str(chars[char]))

main()
