from stats import text_count
from stats import count_character
from stats import sort_character
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except fileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)

    
    book_count = text_count(book_text)
    character_count = count_character(book_text)
    sort_cha = sort_character(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_count} total words")
    print("--------- Character Count -------")
    for item in sort_cha:
        print(f"{item['char']}: {item['num']}")






if __name__ == "__main__":
    main()
