def get_book_text(file_path):
    with open(file_path) as file:
        book_text = file.read()
    list_of_words = book_text.split()
    return len(list_of_words)

def get_book_characters(file_path):
    dict_of_characters = {}
    list_of_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                          "k", "l", "m", "n", "o", "p", "q", "r", "s", 
                          "t", "u", "v", "w", "x", "y", "z","!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".",
                          "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
    with open(file_path) as file:
        book_text = file.read()
    for char in list_of_characters:
        for character in book_text:
            if char == character.lower():
                if char in dict_of_characters:
                    dict_of_characters[char] += 1
                else:
                    dict_of_characters[char] = 1
    # If a character is not found, set its count to 0
    return dict_of_characters
