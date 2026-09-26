from stats import word_count
from stats import letter_count
from stats import chars_dict_to_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contains = f.read() 

    return file_contains

def print_report(book_path,word_cunt,sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_cunt} total words")
    print("--------- Character Count -------")
    for letter,count in sorted_list:
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============= END ===============")




 
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print_report(book_path,word_count(text),chars_dict_to_sorted_list(letter_count(text)))

main()
