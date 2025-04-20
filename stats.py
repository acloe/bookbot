def count_words(text):
    word_list = text.split()
    return(len(word_list))

def char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        char_dict[char] = char_dict.get(char, 0) + 1
    return (char_dict)

def sort_char_count(char_dict):
    chars_list = []
    
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)
    
    def sort_by_count(dict_item):
        return (dict_item["count"])
    
    chars_list.sort(reverse=True, key=sort_by_count)
    return(chars_list)

def print_format_char(number_of_words, sorted_char_dict, path_of_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_of_book}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_char_dict:
        char = dict["char"]
        count = dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
                