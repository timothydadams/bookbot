import sys
import argparse
from stats import get_words_list, build_character_dict, build_sorted_list

parser = argparse.ArgumentParser(description="A simple program to count words and characters in a text file.")
parser.add_argument("path", help="path to text file")
parser.add_argument("-a", "--alpha-chars-only", help="include non-alpha characters", default="True")
args = parser.parse_args()

alphaOnlyFlag = eval(args.alpha_chars_only)
print(args, alphaOnlyFlag)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    # path = input("enter relative filepath to book (ie ./books/title.txt): ")
    if (len(sys.argv) == 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = args.path
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
        # print(f"'{char}'")
        if alphaOnlyFlag == True and char.isalpha() == False:
            continue
        else:
            print(f"{char}: {count}")
        # if ((alphaOnlyFlag == True and char.isalpha()) or (alphaOnlyFlag==False)):
            

    print("============= END ===============")

main()