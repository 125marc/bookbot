from stats import get_book_text, get_book_characters
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_book_text(sys.argv[1])} total words")
    print(f"--------- Character Count -------")
    for k, i in get_book_characters(sys.argv[1]).items():
        print(f"{k}: {i}")

main()
