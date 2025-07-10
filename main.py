from stats import count_words, count_characters, ordered_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         from sys import exit
         sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    character_count = count_characters(book_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = ordered_dict(character_count)
    for char_info in sorted_chars:
        char = char_info["character"]
        count = char_info["count"]
        if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")

main()


