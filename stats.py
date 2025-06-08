

def get_book_text(file_path):
    with open(file_path) as file:
        book_text = file.read()
    list_of_words = book_text.split()
    return len(list_of_words)