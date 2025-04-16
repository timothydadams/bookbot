from sys import argv, exit
from stats import get_words_list, build_character_dict, build_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    # path = input("enter relative filepath to book (ie ./books/title.txt): ")
    if (len(argv) == 1):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path = argv[1]
    text = get_book_text(path)
    words = get_words_list(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("--------- Character Count -------")

    char_list = build_character_dict(text)
    sorted_list = build_sorted_list(char_list)
    for item in sorted_list:
        char = item["char"]
        count = item["frequency"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()