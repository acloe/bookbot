from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    #print(f"{num_words} words found in the document")
    #print(char_count(book_text))
    num_char_dict = char_count(book_text)
    num_char_dict = sort_char_count(num_char_dict)
    #print(num_char_dict)
    
    print_format_char(num_words, num_char_dict, book_path)
    

main()    